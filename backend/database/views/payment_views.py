from rest_framework import viewsets
from database.models import Payment
from database.serializers import PaymentSerializer  

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer  