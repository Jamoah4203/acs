from rest_framework import viewsets
from database.models import Employee
from database.serializers import EmployeeSerializer  

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer  