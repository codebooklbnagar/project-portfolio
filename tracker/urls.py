from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_ip, name='get_ip'),
]
