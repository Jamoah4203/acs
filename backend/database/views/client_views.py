from rest_framework import viewsets
from database.models import Client
from database.serializers import ClientSerializer  

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  