from rest_framework import viewsets
from database.models import Expense
from database.serializers import ExpenseSerializer  

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer  