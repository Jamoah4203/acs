from rest_framework import viewsets
from database.models import Admin
from database.serializers import AdminSerializer  

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer  