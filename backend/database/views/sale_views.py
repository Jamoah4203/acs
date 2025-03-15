from rest_framework import viewsets
from database.models import Sale
from database.serializers import SaleSerializer  

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer  