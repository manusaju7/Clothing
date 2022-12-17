
from django.urls import path

from clothing_app import views

urlpatterns = [
    path('', views.demo, name='demo')
]