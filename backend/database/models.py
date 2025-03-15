from django.db import models
from django.contrib.auth.hashers import make_password

# Employee Table
class Employee(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('management', 'Management'),
        ('operations', 'Operations'),
        ('sales', 'Sales'),
        ('transport', 'Transport'),
        ('accounting', 'Accounting')
    ]
    full_name = models.CharField(max_length=191)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

# Admin Table
class Admin(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk or not Admin.objects.filter(pk=self.pk, password=self.password).exists():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

# Suppliers Table
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    tin = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Product Table
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_stock_quantity(self):
        purchases = PurchaseTransaction.objects.filter(product=self).aggregate(total=models.Sum('quantity'))['total'] or 0
        sales = SaleTransaction.objects.filter(product=self).aggregate(total=models.Sum('quantity'))['total'] or 0
        return purchases - sales

    def save(self, *args, **kwargs):
        self.stock_quantity = self.get_stock_quantity()
        super().save(*args, **kwargs)

# Clients Table
class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Purchases Table
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transportation_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

# Purchase Transactions Table
class PurchaseTransaction(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InventoryLog.log_transaction(self.product, "Purchase", self.quantity)

# Sales Table
class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    sales_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    invoice_number = models.CharField(max_length=15, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last_invoice = Sale.objects.order_by('-id').first()
            last_number = int(last_invoice.invoice_number.split('-')[-1]) + 1 if last_invoice and last_invoice.invoice_number else 1
            self.invoice_number = f"INV-{str(last_number).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number

# Sale Transactions Table
class SaleTransaction(models.Model):
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        InventoryLog.log_transaction(self.product, "Sale", -self.quantity)

# Payments Table
class Payment(models.Model):
    TRANSACTION_TYPE = [('Sales', 'Sales'), ('Purchase', 'Purchase')]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

# Inventory Log Table
class InventoryLog(models.Model):
    CHANGE_TYPE = [('Purchase', 'Purchase'), ('Sale', 'Sale')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=10, choices=CHANGE_TYPE)
    quantity_changed = models.IntegerField()
    log_date = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def log_transaction(product, change_type, quantity):
        InventoryLog.objects.create(product=product, change_type=change_type, quantity_changed=quantity)

# Transport Table
class Transport(models.Model):
    TRANSACTION_TYPE = [('Purchase', 'Purchase'), ('Sales', 'Sales')]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    driver_name = models.CharField(max_length=255, blank=True, null=True)
    vehicle_number = models.CharField(max_length=50, blank=True, null=True)
    from_location = models.TextField()
    to_location = models.TextField()
    transport_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_status = models.CharField(max_length=10, choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)


# Reports Table
class Report(models.Model):
    REPORT_TYPE = [('Sales', 'Sales'), ('Purchases', 'Purchases'), ('Inventory', 'Inventory'), ('Profit', 'Profit'), ('Client Analysis', 'Client Analysis'), ('Expenditure', 'Expenditure')]
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE)
    report_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

# Expense Table
class Expense(models.Model):
    expense_type = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()