from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'main/home.html')

def riyadh_view(request):
    return render(request, 'main/riyadh.html')

def jeddah_view(request):
    return render(request, 'main/jeddah.html')

def khobar_view(request):
    return render(request, 'main/khobar.html')

def medina_view(request):
    return render(request, 'main/medina.html')

def mecca_view(request):
    return render(request, 'main/mecca.html')

def jazan_view(request):
    return render(request, 'main/jazan.html')

def aseer_view(request):
    return render(request, 'main/aseer.html')

def aljouf_view(request):
    return render(request, 'main/aljouf.html')

def tabuk_view(request):
    return render(request, 'main/aljouf.html')

def alula_view(request):
    return render(request, 'main/alula.html')

def taif_view(request):
    return render (request, 'main/taif.html')

def discover_view(request):
    return render (request, "main/discover.html")