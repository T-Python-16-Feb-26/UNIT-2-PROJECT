from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .data_tourist import TOURIST_CITIES
from .data_investor import INVESTOR_CITIES
# Create your views here.




def get_lang(request: HttpRequest) -> str:
    """Return current language from cookie, default to Arabic."""
    return request.COOKIES.get('lang', 'ar')


def get_persona(request: HttpRequest):
    """Return current persona from cookie: 'tourist' or 'investor'."""
    return request.COOKIES.get('persona', None)


# - - - views - - -

def persona_view(request: HttpRequest) -> HttpResponse:
    """Landing page — choose persona (tourist or investor)."""

    if request.method == 'POST':
        selected = request.POST.get('persona')  # 'tourist' or 'investor'
        if selected in ['tourist', 'investor']:
            response = redirect('home_view')
            response.set_cookie('persona', selected, max_age=60*60*12)  #  12h
            return response

    lang = get_lang(request)
    return render(request, 'main/persona.html', {'lang': lang})


def home_view(request: HttpRequest) -> HttpResponse:
    """Home page — show cities based on persona cookie."""

    persona_val = get_persona(request)

    #if no persona selected, redirect to persona selection
    if not persona_val:
        return redirect('persona_view')

    lang = get_lang(request)

    if persona_val == 'tourist':
        cities = TOURIST_CITIES
    else:
        cities = INVESTOR_CITIES

    context = {
        'cities': cities,
        'persona': persona_val,
        'lang': lang,
    }
    return render(request, 'main/home.html', context)


def city_detail_view(request: HttpRequest, city_slug: str) -> HttpResponse:
    """City detail page — show places or projects inside a city."""

    persona_val = get_persona(request)

    if not persona_val:
        return redirect('persona_view')

    lang = get_lang(request)

    if persona_val == 'tourist':
        cities = TOURIST_CITIES
        items_key = 'places'
    else:
        cities = INVESTOR_CITIES
        items_key = 'projects'

    # Find the city by slug
    city = next((c for c in cities if c['slug'] == city_slug), None)

    # If city not found, redirect to home
    if not city:
        return redirect('home_view')

    context = {
        'city': city,
        'items': city[items_key],
        'items_key': items_key,
        'persona': persona_val,
        'lang': lang,
    }
    return render(request, 'main/city_detail.html', context)


def item_detail_view(request: HttpRequest, city_slug: str, item_type: str, item_id: int) -> HttpResponse:
    """Item detail page — show details of a place or project."""

    persona_val = get_persona(request)

    if not persona_val:
        return redirect('persona_view')

    lang = get_lang(request)

    if persona_val == 'tourist':
        cities = TOURIST_CITIES
        items_key = 'places'
    else:
        cities = INVESTOR_CITIES
        items_key = 'projects'

    # - - Find the city - -
    city = next((c for c in cities if c['slug'] == city_slug), None)
    if not city:
        return redirect('home_view')

    # - - Find the item by id - -
    item = next((i for i in city[items_key] if i['id'] == item_id), None)
    if not item:
        return redirect('city_detail_view', city_slug=city_slug)

    context = {
        'city': city,
        'item': item,
        'item_type': item_type,
        'persona': persona_val,
        'lang': lang,
    }
    return render(request, 'main/item_detail.html', context)


def about_view(request: HttpRequest) -> HttpResponse:
    """About page."""

    persona_val = get_persona(request)
    lang = get_lang(request)

    context = {
        'persona': persona_val,
        'lang': lang,
    }
    return render(request, 'main/about.html', context)


def set_language_view(request: HttpRequest) -> HttpResponse:
    """Set language cookie and redirect back to previous page."""

    lang = request.GET.get('lang', 'ar')
    if lang not in ['ar', 'en']:
        lang = 'ar' #by default ar

    next_url = request.GET.get('next', '/')
    response = redirect(next_url)
    response.set_cookie('lang', lang, max_age=60*60*48)  # 2 days
    return response


def change_persona_view(request: HttpRequest) -> HttpResponse:
    """Clear persona cookie and redirect to persona selection."""

    response = redirect('persona_view')
    response.delete_cookie('persona')
    return response