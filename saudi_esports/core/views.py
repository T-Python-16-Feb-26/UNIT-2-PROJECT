from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest):
    return render(request, 'core/home.html')


def about_view(request: HttpRequest):
    return render(request, 'core/about.html')


def games_view(request: HttpRequest):
    return render(request, 'core/games.html')


def teams_view(request: HttpRequest):
    return render(request, 'core/teams.html')


def infrastructure_view(request: HttpRequest):
    return render(request, 'core/infrastructure.html')


def timeline_view(request: HttpRequest):
    return render(request, 'core/timeline.html')


def events_view(request: HttpRequest):
    return render(request, 'core/events.html')


def home_view(request: HttpRequest):
    theme = request.COOKIES.get("theme", "dark")

    response = render(request, 'core/home.html', {
        'theme': theme
    })

    return response