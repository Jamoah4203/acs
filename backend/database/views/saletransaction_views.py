from rest_framework import viewsets
from database.models import SaleTransaction
from database.serializers import SaleTransactionSerializer  

class SaleTransactionViewSet(viewsets.ModelViewSet):
    queryset = SaleTransaction.objects.all()
    serializer_class = SaleTransactionSerializer  