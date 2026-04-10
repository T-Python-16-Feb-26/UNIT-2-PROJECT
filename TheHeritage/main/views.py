from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def home_view(request:HttpRequest):

    return render(request, 'main/index.html')


def clothing_view(request:HttpRequest):

    return render(request,'main/clothing.html')  

def foods_view(request:HttpRequest):

    return render(request,'main/foods.html')  

def game_view(request:HttpRequest):

    return render(request,'main/game.html')
