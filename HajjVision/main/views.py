from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

ALLOWED_THEMES = {"light", "dark"}

# Create your views here.

def set_theme(request):
    """Read ?theme= from the URL, set a cookie, redirect back."""
    theme = request.GET.get("theme", "light")
    if theme not in ALLOWED_THEMES:
        theme = "light"

    # redirect
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"

    response = redirect(next_url)
    response.set_cookie(
        key="theme",
        value=theme,
        max_age=60 * 60 * 24 * 365,  
        httponly=False,         
        samesite="Lax",
    )
    return response


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def focus(request):
    return render(request, 'main/focus.html')


def targets(request):
    return render(request, 'main/targets.html')


def baseline(request):
    return render(request, 'main/baseline.html')


def strategy(request):
    return render(request, 'main/strategy.html')


