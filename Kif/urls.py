from django.urls import path, include
from django.contrib import admin
from products.views import ProductList
# from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList, name='list of products'),
    path('<str:category_name>/', include('products.urls'))
]


# path('api/', include('api.urls'), name='api page'),
# path('basket/', include('basket.urls')),
# path('hello/', hello_world, name='first page hello'),
# path('Products/', include('products.urls'), name=('list of products'),

