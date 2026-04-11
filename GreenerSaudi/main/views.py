from django.http import HttpRequest
from django.shortcuts import redirect, render


def home_view(request: HttpRequest):
    return render(request, 'main/home.html')

def about_view(request: HttpRequest):
    return render(request, 'main/about.html')

def impact_view(request: HttpRequest):
    return render(request, 'main/impact.html')

def progress_view(request: HttpRequest):
    return render(request, 'main/progress.html')

def goal_view(request: HttpRequest):
    return render(request, 'main/goal.html')

def get_involved_view(request: HttpRequest):
    return render(request, 'main/get_involved.html')

def news_view(request: HttpRequest):
    return render(request, 'main/news.html')

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')

def mode_view(request: HttpRequest, mode: str):
    response = redirect(request.GET.get('next', '/'))

    if mode == 'light':
        response.set_cookie('mode', 'light')
    elif mode == 'dark':
        response.set_cookie('mode', 'dark')

    return response
