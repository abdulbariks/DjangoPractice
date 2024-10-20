from django.shortcuts import render
from django.http import HttpResponse

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


