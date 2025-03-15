from rest_framework import viewsets
from database.models import InventoryLog
from database.serializers import InventoryLogSerializer  

class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer  