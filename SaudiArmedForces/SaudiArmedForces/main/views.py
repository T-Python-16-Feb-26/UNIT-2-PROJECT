from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request : HttpRequest):
    return render(request,"main/home.html")


def land_forces_view(request : HttpRequest):
    return render(request,"main/land_forces.html")


def air_forces_view(request : HttpRequest):
    return render(request,"main/air_forces.html")


def naval_forces_view(request : HttpRequest):
    return render(request,"main/naval_forces.html")


def air_defense_forces_view(request : HttpRequest):
    return render(request,"main/air_defense_forces.html")


def strategic_missile_force_view(request : HttpRequest):
    return render(request,"main/strategic_missile_force.html")


def military_system_view(request : HttpRequest):
    return render(request,"main/military_system.html")


def heroes_view(request : HttpRequest):
    return render(request,"main/heroes.html")


def technology_view(request : HttpRequest):
    return render(request,"main/technology.html")

def mode_view(request : HttpRequest,mode):
    response = redirect(request.GET.get("next","/"))

    if mode == "light":
        response.set_cookie("mode","light")
    elif mode == "dark":
        response.set_cookie("mode","dark")

    return response
