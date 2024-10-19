from django.urls import path
from . import views

urlpatterns = [
    path('deep/', views.deepLearning, name='deepLearning'),
]