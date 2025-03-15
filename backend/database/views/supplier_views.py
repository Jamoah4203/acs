from rest_framework import viewsets
from database.models import Supplier
from database.serializers import SupplierSerializer  

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer  