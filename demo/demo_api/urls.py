from .views import DemoListApiView
from django.urls import path



urlpatterns = [
    path('api/', DemoListApiView.as_view()),
]