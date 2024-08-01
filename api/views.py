'''
from django.shortcuts import render
from rest_framework import generics
# from aproduct.models import Product
from .serializers import ProductSerializer

class ProductListSerializer(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
'''