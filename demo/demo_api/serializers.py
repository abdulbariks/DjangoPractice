from rest_framework import serializers
from .models import Demo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = ["task", "completed", "timestamp", "updated", "user"]