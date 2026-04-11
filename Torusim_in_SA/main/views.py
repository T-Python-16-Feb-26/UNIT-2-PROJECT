from django.shortcuts import render
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


    context = {
        "event_slides": event_slides
    }
    return render(request, 'main/home_view.html',context)


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

def experience_detail(request: HttpRequest, slug: str):
    json_path = Path(__file__).resolve().parent / "data" / "experiences.json"

    with open(json_path, "r", encoding="utf-8") as file:
        experiences = json.load(file)

    experience = next((item for item in experiences if item.get("slug") == slug), None)

    if not experience:
        raise Http404("Experience not found")

    return render(request, "main/experience_detail.html", {"experience": experience})
