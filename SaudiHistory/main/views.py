from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.

def home_view(request:HttpRequest) :
    return render(request, 'main/home.html')


def state1_view(request: HttpRequest):
    return render(request, 'main/first_saudi_state.html')

def state2_view(request: HttpRequest):
    return render(request, 'main/second_saudi_state.html')

def state3_view(request: HttpRequest):
    return render(request, 'main/saudi_arabia_kingdom.html')



def king1_view(request:HttpRequest) :
    return render(request, 'main/king_abdulaziz.html')

def king2_view(request:HttpRequest) :
    return render(request, 'main/king_saud.html')
    
def king3_view(request: HttpRequest):
    return render(request, 'main/king_faisal.html')

def king4_view(request: HttpRequest):
    return render(request, 'main/king_khalid.html')

def king5_view(request: HttpRequest):
    return render(request, 'main/king_fahd.html')

def king6_view(request: HttpRequest):
    return render(request, 'main/king_abdullah.html')

def king7_view(request: HttpRequest):
    return render(request, 'main/king_salman.html')


def light_mode_view(request: HttpRequest):
    response = redirect("main:home_view")
    response.set_cookie("mode", "light", max_age=60*60*24 )
    return response

def dark_mode_view(request: HttpRequest):
    response = redirect("main:home_view") 
    response.set_cookie("mode", "dark", max_age=-3600 )
    return response

