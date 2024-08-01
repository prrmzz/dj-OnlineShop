from django.urls import path
from .views import parham, productlist, iphone13

urlpatterns = [
    path('add/', parham),
    path('list/', productlist, name='prlist'),
    path('list/iphone13/', iphone13, name='ip13')
]
