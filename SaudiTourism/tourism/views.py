from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
# home_page 
def home_view(request: HttpRequest):
    return render(request, 'tourism/home_page.html')
# riyadh_page
def riyadh_view(request:HttpRequest,):
    return render (request, 'tourism/riyadh_page.html')
# makkah_page
def makkah_view(request:HttpRequest,):
    return render (request, 'tourism/makkah_page.html')
# madinah_page
def madinah_view(request:HttpRequest,):
    return render (request, 'tourism/madinah_page.html')
# qassim_page
def qassim_view(request:HttpRequest,):
    return render (request, 'tourism/qassim_page.html')
# jeddah_page
def jeddah_view(request:HttpRequest,):
    return render (request, 'tourism/jeddah_page.html')
# alula_page
def alula_view(request:HttpRequest,):
    return render (request, 'tourism/alula_page.html')

def mode_view(request:HttpRequest ,mode):
    response = redirect(request.GET.get('next','/'))
    if mode == 'dark':
        response.set_cookie('mode','dark',max_age=60*60*24)
    elif mode == 'light':
        response.set_cookie('mode','light',max_age=60*60*24)
    return response