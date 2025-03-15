from rest_framework import viewsets
from database.models import PurchaseTransaction
from database.serializers import PurchaseTransactionSerializer  

class PurchaseTransactionViewSet(viewsets.ModelViewSet):
    queryset = PurchaseTransaction.objects.all()
    serializer_class = PurchaseTransactionSerializer  