from django.shortcuts import render
from django.shortcuts import HttpResponse

def odd(request):
    c= 12+32
    return HttpResponse(c)

def show(request):
    return HttpResponse("Hello DarazApp")



    
     

# Create your views here.
