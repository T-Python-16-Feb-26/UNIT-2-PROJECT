from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json
from pathlib import Path


# Create your views here.
def load_events():
    file_path = Path(__file__).resolve().parent / "data" / "events.json"
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

    riyadh_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "riyadh"
    ]

    riyadh_event_slides = chunk_list(riyadh_events, 3)

    context = {
        "riyadh_events": riyadh_events,
        "riyadh_event_slides": riyadh_event_slides,
    }

    
    return render(request, 'main/riyadh.html',context)


def jeddah_view(request:HttpRequest):

    events = load_events()

    jeddah_events = [
        event for event in events
        if event.get("city", "").strip().lower() == "jeddah"
    ]

    jeddah_event_slides = chunk_list(jeddah_events, 3)

    context = {
        "jeddah_events": jeddah_events,
        "jeddah_event_slides": jeddah_event_slides,
    }

    
    return render(request, 'main/jeddah.html',context)