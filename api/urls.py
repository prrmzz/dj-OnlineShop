from django.urls import path, include
from .views import MainSerializer

urlpatterns = [
    path('main/', MainSerializer),
]