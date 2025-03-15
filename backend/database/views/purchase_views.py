from rest_framework import viewsets
from database.models import Purchase
from database.serializers import PurchaseSerializer  

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer  