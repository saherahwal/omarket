from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

def hello(request):
    return HttpResponse("Hello world")

def homepage(request):    
    return render( request , "index.html", {})

#
# pricing view and packages
#
def pricing(request):
    return render( request, "pricing.html", {})
