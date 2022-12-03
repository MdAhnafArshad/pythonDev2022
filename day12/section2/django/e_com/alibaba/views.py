from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("welcome to Alibaba response Index Function with HttpResponse")
    

# Create your views here.
