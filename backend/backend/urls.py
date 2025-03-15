"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from database.views.admin_views import AdminViewSet
from database.views.client_views import ClientViewSet
from database.views.product_views import ProductViewSet
from database.views.employee_views import EmployeeViewSet
from database.views.supplier_views import SupplierViewSet
from database.views.payment_views import PaymentViewSet
from database.views.sale_views import SaleViewSet
from database.views.purchase_views import PurchaseViewSet
from database.views.transport_views import TransportViewSet
from database.views.expense_views import ExpenseViewSet
from database.views.report_views import ReportViewSet
from database.views.inventorylog_views import InventoryLogViewSet
from database.views.purchasetransaction_views import PurchaseTransactionViewSet
from database.views.saletransaction_views import SaleTransactionViewSet
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the homepage!")


# Initialize Router
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'purchase-transactions', PurchaseTransactionViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'sales-transactions', SaleTransactionViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'reports', ReportViewSet)

# URL Patterns
urlpatterns = [
    path('', home, name='home'),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]