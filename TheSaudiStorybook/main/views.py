from django.http import HttpRequest
from django.shortcuts import render

# Main view for the home page
def home_view(request: HttpRequest):
    
    return render(request, 'main/home.html')

# Land view for the land chapter
def land_view(request: HttpRequest):
    
    return render(request, 'main/land.html')

# People view for the people chapter
def people_view(request: HttpRequest):
    
    return render(request, 'main/people.html')

# Traditions view for the traditions chapter
def traditions_view(request: HttpRequest):
    
    return render(request, 'main/traditions.html')

# Cities view for the cities chapter
def cities_view(request: HttpRequest):
    
    return render(request, 'main/cities.html')

# Royal Family view for the royal family chapter
def royal_family_view(request: HttpRequest):
    
    return render(request, 'main/royal-family.html')

# Future view for the future chapter
def future_view(request: HttpRequest):
    
    return render(request, 'main/future.html')

# Legacy view for the legacy chapter
def legacy_view(request: HttpRequest):
    
    return render(request, 'main/legacy.html')

# Celebrations view for the celebrations chapter
def celebrations_view(request: HttpRequest):
    
    return render(request, 'main/celebrations.html')