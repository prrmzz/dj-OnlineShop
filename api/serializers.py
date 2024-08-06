from rest_framework.serializers import ModelSerializer
from products.models import Product


class MainSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

