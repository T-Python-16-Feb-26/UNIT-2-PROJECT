# Imports
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'main/home.html')

def crops_view(request):
    return render(request, 'main/crops.html')

def regions_view(request):
    return render(request, 'main/regions.html')

def initiatives_view(request):
    return render(request, 'main/initiatives.html')

def technology_view(request):
    return render(request, 'main/technology.html')

def records_view(request):
    return render(request, 'main/records.html')

def facts_view(request):
    return render(request, 'main/facts.html')

def quiz_view(request):
    return render(request, 'main/quiz.html')
