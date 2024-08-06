from django.http import JsonResponse, HttpResponse
from products.models import Product, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer


@api_view(['GET'])
def ProductList(request):
    productlist = Product.objects.all()
    productlist_serializer = ProductSerializer(productlist, many=True)
    return Response(productlist_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def CategorySelf(request, category_name):
    normalized_category_name = category_name.replace('-', ' ')
    try:
        categoryself = Category.objects.get(name__iexact=normalized_category_name)
        categoryself_products = Product.objects.filter(category_id=categoryself)
        categoryself_serializer = ProductSerializer(categoryself_products, many=True)
        return Response(categoryself_serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ProductSelf(request, product_name, category_name):
    normalized_product_name = product_name.replace('-', ' ')
    normalized_category_name = category_name.replace('-', ' ')
    try:
        productself = Product.objects.get(name__iexact=normalized_product_name)
        categoryself = Category.objects.get(name__iexact=normalized_category_name)
        if productself.category_id == categoryself:
            productself_serializer = ProductSerializer(productself, many=False)
            return Response(productself_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Product doesn't exist in this category"}, status=status.HTTP_404_NOT_FOUND)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

