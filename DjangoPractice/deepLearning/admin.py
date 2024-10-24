from django.contrib import admin

from .models import DeepLearning

# Register your models here.
class DeepLearningAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname",)

admin.site.register(DeepLearning, DeepLearningAdmin)
