from django.shortcuts import render
from pip._vendor.requests import request

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request,'contact.html')