from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    
    return render(request, 'main/home_view.html')


def destinations_view(request:HttpRequest):

    return render(request, 'main/destinations.html')

def riyadh_view(request:HttpRequest):

    return render(request, 'main/riyadh.html')