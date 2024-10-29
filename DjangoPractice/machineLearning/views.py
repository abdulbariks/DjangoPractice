from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def machineLearning(request):
    name = "Abdul Barik"
    age = 28
    fruits= ['Apple', 'Banana', 'Cherry']   
    person  = {
        "name" : name,
        "age":age,
        "fruits": fruits,
    }
    return render(request, "machineLearning/machineLearning.html", context=person) 

def main(request):
    return render(request, "main.html") 


def registration(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:    
        fm = UserCreationForm()
    return render(request, 'machineLearning/register.html', {'form':fm})
    

