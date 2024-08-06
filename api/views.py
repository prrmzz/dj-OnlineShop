from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from .serializers import MainSerializer


class ProductListSerializer(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = MainSerializer
