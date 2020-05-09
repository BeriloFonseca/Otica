from django.shortcuts import render
from pip._vendor.requests import request

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')

def store1(request):
    return render(request,'store1.html')

def store2(request):
    return render(request,'store2.html')

def store3(request):
    return render(request,'store3.html')


