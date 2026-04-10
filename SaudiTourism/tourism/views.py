from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    return render(request, 'tourism/home_page.html')

def riyadh_view(request:HttpRequest,):
    return render (request, 'tourism/riyadh_page.html')

def makkah_view(request:HttpRequest,):
    return render (request, 'tourism/makkah_page.html')

def madinah_view(request:HttpRequest,):
    return render (request, 'tourism/madinah_page.html')

def qassim_view(request:HttpRequest,):
    return render (request, 'tourism/qassim_page.html')