from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404
import json
from pathlib import Path


# Create your views here.
def load_events():
    file_path = Path(__file__).resolve().parent / "data" / "events.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    

def load_experiences():
    file_path = Path(__file__).resolve().parent / "data" / "experiences.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def chunk_list(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]



def home_view(request:HttpRequest):
    events = load_events()
    event_slides = chunk_list(events, 3)

    experience = load_experiences()
    experience_slides = chunk_list(experience, 3)

    context = {
        "event_slides": event_slides,
        "experience_slides": experience_slides
    }

    return render(request, 'main/home_view.html', context )


def destinations_view(request:HttpRequest):

    return render(request, 'main/destinations.html')

def riyadh_view(request:HttpRequest):

    events = load_events()
    experiences = load_experiences()

    riyadh_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "riyadh"
    ]

    riyadh_experiences = [
        exp for exp in experiences
        if exp.get("city", "").strip().lower() == "riyadh"
    ]


    riyadh_event_slides = chunk_list(riyadh_events, 3)
    riyadh_experience_slides = chunk_list(riyadh_experiences, 3)


    context = {
        "riyadh_events": riyadh_events,
        "riyadh_event_slides": riyadh_event_slides,
        "riyadh_experiences": riyadh_experiences,
        "riyadh_experience_slides": riyadh_experience_slides,
    }

    
    return render(request, 'main/riyadh.html',context)


def jeddah_view(request: HttpRequest):
    events = load_events()
    experiences = load_experiences()

    jeddah_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "jeddah"
    ]
    jeddah_experiences = [
        exp for exp in experiences
        if exp.get("city", "").strip().lower() == "jeddah"
    ]

    jeddah_event_slides = chunk_list(jeddah_events, 3)
    jeddah_experience_slides = chunk_list(jeddah_experiences, 3)

    context = {
        "jeddah_events": jeddah_events,
        "jeddah_event_slides": jeddah_event_slides,
        "jeddah_experiences": jeddah_experiences,
        "jeddah_experience_slides": jeddah_experience_slides,
    }
    return render(request, 'main/jeddah.html', context)

def alula_view(request: HttpRequest):
    events = load_events()
    experiences = load_experiences()

    alula_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "alula"
    ]
    alula_experiences = [
        exp for exp in experiences
        if exp.get("city", "").strip().lower() == "alula"
    ]

    alula_event_slides = chunk_list(alula_events, 3)
    alula_experience_slides = chunk_list(alula_experiences, 3)

    context = {
        "alula_events": alula_events,
        "alula_event_slides": alula_event_slides,
        "alula_experiences": alula_experiences,
        "alula_experience_slides": alula_experience_slides,
    }
    return render(request, 'main/alula.html', context)

def abha_view(request: HttpRequest):
    events = load_events()
    experiences = load_experiences()

    abha_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "abha"
    ]
    abha_experiences = [
        exp for exp in experiences
        if exp.get("city", "").strip().lower() == "abha"
    ]

    abha_event_slides = chunk_list(abha_events, 3)
    abha_experience_slides = chunk_list(abha_experiences, 3)

    context = {
        "abha_events": abha_events,
        "abha_event_slides": abha_event_slides,
        "abha_experiences": abha_experiences,
        "abha_experience_slides": abha_experience_slides,
    }
    return render(request, 'main/abha.html', context)

def experience_detail(request: HttpRequest, slug: str):
    json_path = Path(__file__).resolve().parent / "data" / "experiences.json"

    with open(json_path, "r", encoding="utf-8") as file:
        experiences = json.load(file)

    experience = next((item for item in experiences if item.get("slug") == slug), None)

    if not experience:
        raise Http404("Experience not found")

    return render(request, "main/experience_detail.html", {"experience": experience})

def contact_view(request:HttpRequest):

    return render(request, 'main/contact_us.html')

def about_view(request:HttpRequest):

    return render(request, 'main/about_us.html')

def terms_view(request:HttpRequest):

    return render(request, 'main/terms.html')


def large_font(request: HttpRequest):

    response = redirect(request.GET.get("next"))
    response.set_cookie('font','large', max_age=60*60*24)

    return response

def small_font(request: HttpRequest):

    response = redirect(request.GET.get("next"))
    response.set_cookie('font','small', max_age=-3600)

    return response

def search_view(request: HttpRequest):
    query = request.GET.get('q', '').strip()
    results = []

    experiences = load_experiences()
    events = load_events()

    for item in experiences:
        item["content_type"] = "experience"

    for item in events:
        item["content_type"] = "event"

    items = experiences + events

    if query:
        query_lower = query.lower()
        results = [
            item for item in items
            if query_lower in item.get('title', '').lower()
            or query_lower in item.get('city', '').lower()
            or query_lower in item.get('category', '').lower()
            or query_lower in item.get('location', '').lower()
            or query_lower in item.get('description', '').lower()
            or query_lower in item.get('slug', '').lower()
            or query_lower in item.get('date', '').lower()
        ]

    return render(request, 'main/search.html', {
        'query': query,
        'results': results,
    })

