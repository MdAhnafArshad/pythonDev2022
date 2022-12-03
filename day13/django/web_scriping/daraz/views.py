from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import TestProduct

 #def odd(request):
    #c= 12+32
    #return HttpResponse(c)



def show(request):
    #return HttpResponse("Hello DarazApp")
    return render(request, 'from.html')


#database puss throuth the data


    ti = "Hello Daraz"
    product = TestProduct(title=ti)
    product.save()
     

# Create your views here.
