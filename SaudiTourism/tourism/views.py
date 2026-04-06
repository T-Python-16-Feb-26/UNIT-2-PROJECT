from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    return render(request, 'tourism/home_page.html')

# def city_view(request:HttpRequest, city_name:str):
#     return render (request, 'tourism/city_page.html', {'city_name': city_name})