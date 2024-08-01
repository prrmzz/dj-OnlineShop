from django.urls import path
from products.views import CategorySelf, ProductSelf


urlpatterns = [
    path('', CategorySelf),
    path('<str:product_name>', ProductSelf),
]
