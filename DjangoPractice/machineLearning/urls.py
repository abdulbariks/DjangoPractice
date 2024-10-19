from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.machineLearning, name='machineLearning'),
]