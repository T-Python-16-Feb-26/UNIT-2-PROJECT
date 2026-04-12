from django.shortcuts import render,redirect
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

def handicrafts_view(request:HttpRequest):

    return render(request, 'main/handicrafts.html')

def folk_arts_view(request: HttpRequest):

    return render(request, 'main/folkarts.html')

def traditions_view(request: HttpRequest):

    return render(request, 'main/traditions.html')


def mode_view(request:HttpRequest,mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light", max_age=60*60*24*7)

    elif mode == "dark":
        response.set_cookie("mode", "dark", max_age=60*60*24*7)


    return response
