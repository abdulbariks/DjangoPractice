from django.urls import path
from . import views

urlpatterns = [
    path('machineLearning/', views.machineLearning, name='machineLearning'),
]