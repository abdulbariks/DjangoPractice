from django.shortcuts import render
from django.http import HttpResponse

from .models import DeepLearning

# Create your views here.
def deepLearning(request):
    deeplearnings = DeepLearning.objects.all().values()
    context = {
        'deeplearnings' : deeplearnings,
    }
    print(deeplearnings)
    return render(request, "deepLearning/deepLearning.html", context ) 