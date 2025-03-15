from rest_framework import viewsets
from database.models import Product
from database.serializers import ProductSerializer  

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  