from django.urls import path
from . import views

urlpatterns = [
    path('deepLearning/', views.deepLearning, name='deepLearning'),
]