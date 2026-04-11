from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.

def persona_view(request:HttpResponse):
    return render(request,'main/persona.html')

def set_persona(request):
    response=redirect('home')
    response.set_cookie('user_persona','user_type',max_age=60*60*24)
    return response

def home_view(request):
    persona= request.COOKIES.get('user_persona')
