from rest_framework import viewsets
from database.models import Transport
from database.serializers import TransportSerializer  

class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer  