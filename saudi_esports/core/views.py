from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request:HttpRequest):
    return render(request, 'core/home.html')

def base_view(request:HttpRequest):
    return render(request, 'core/base.html')

def about_view(request:HttpRequest):
    return render(request, 'core/about.html')

def game_view(request:HttpRequest):
    return render(request, 'core/game.html')

def teams_view(request:HttpRequest):
    return render(request, 'core/teams.html')

def infrastructure_view(request:HttpRequest):
    return render(request, 'core/infrastructure.html')

def timeline_view(request:HttpRequest):
    return render(request, 'core/timeline.html')

def events_view(request:HttpRequest):
    return render(request, 'core/events.html')