from django.urls import path
from . import views

urlpatterns = [
    path('machine/', views.machineLearning, name='machineLearning'),
    path('', views.main),
    path('register/', views.registration, name='registration'),
]