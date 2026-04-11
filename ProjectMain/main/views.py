import json
from django.shortcuts import render, redirect
from django.http import Http404
from . import data


def home_view(request):
    return render(request, 'main/home.html', {
        'classes_list': data.CLASSES_LIST,
    })


def class_view(request, class_slug):
    animal_class = data.CLASSES.get(class_slug)
    if not animal_class:
        raise Http404("Animal class not found")
    species_list = [data.SPECIES[s] for s in animal_class['species'] if s in data.SPECIES]

    # Build province → list of species (slug, name, scientific_name, slug) for map interaction
    province_data = {}
    for sp in species_list:
        for prov in sp.get('provinces', []):
            if prov not in province_data:
                province_data[prov] = []
            province_data[prov].append({
                'slug': sp['slug'],
                'name': sp['name'],
                'scientific_name': sp['scientific_name'],
                'image': sp.get('image'),
            })

    return render(request, 'main/class.html', {
        'animal_class': animal_class,
        'species_list': species_list,
        'featured_slugs': data.FEATURED_SLUGS,
        'province_data_json': json.dumps(province_data),
    })


def species_detail_view(request, slug):
    species = data.SPECIES.get(slug)
    if not species:
        raise Http404("Species not found")
    extra = data.FEATURED_EXTRA.get(slug)
    return render(request, 'main/species_detail.html', {
        'species': species,
        'extra': extra,
    })


def set_preference(request, key, value):
    allowed = {
        'theme': ['dark', 'light'],
    }
    redirect_url = request.META.get('HTTP_REFERER', '/')
    if key not in allowed or value not in allowed[key]:
        return redirect(redirect_url)
    response = redirect(redirect_url)
    response.set_cookie(key, value, max_age=60 * 60 * 24 * 365, samesite='Lax')
    return response


def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)
