from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from products.views import ProductList
from django.conf import settings
# from rest_framework import routers


urlpatterns = [

    path('admin/', admin.site.urls),
    path('main/', ProductList, name='list of products'),
    path('main/<str:category_name>/', include('products.urls')),

] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)


# path('basket/', include('basket.urls')),
# path('hello/', hello_world, name='first page hello'),
# path('Products/', include('products.urls'), name=('list of products'),

