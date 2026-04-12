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

# ============= featured non dynamic views =============
def caracal_view(request):
    species = {
       "slug": "caracal",
        "name": "Caracal",
        "scientific_name": "Caracal caracal",
        "class": "mammals",
        "short_description": (
            "A medium-sized wild cat famed for its distinctive tufted ears and "
            "extraordinary leaping ability when hunting birds mid-flight."
        ),
        "habits_lifestyle": "Caracals are solitary animals except during mating and the rearing of young, with both sexes being territorial. They are typically nocturnal and highly secretive, making them difficult to observe in the wild. Their most remarkable hunting feat is their ability to leap up to 3 metres into the air to snatch birds in flight, sometimes catching as many as 12 in a single bound. Fast and powerful, they can tackle prey up to three times their own size. Their ears are controlled by around 20 muscles, giving them exceptional directional hearing for locating prey, and the distinctive tufts on their ear tips are thought to aid in this further.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caracal",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Caracal_on_the_road%2C_early_morning_in_Kgalagadi_%2836173878220%29_%28cropped%29.jpg/500px-Caracal_on_the_road%2C_early_morning_in_Kgalagadi_%2836173878220%29_%28cropped%29.jpg",
        "provinces": ["asir", "makkah", "riyadh"],
    }
    return render(request, "main/caracal.html", {"species": species})



def arabian_oryx_view(request):
    species = {
        "slug": "arabian-oryx",
        "name": "Arabian Oryx",
        "scientific_name": "Oryx leucoryx",
        "class": "mammals",
        "short_description": (
            "A majestic white antelope and the national animal of Saudi Arabia, once extinct in the wild "
            "and brought back through one of conservation's greatest success stories. "
            "Its almost luminous white coat reflects the sun's rays, a vital adaptation to desert life."
        ),
        "habits_lifestyle": (
            "Arabian oryx are gregarious animals and typically form herds of 5 to 30. They are active mostly "
            "in the early morning and late evening, resting in groups in the shade during the searing midday heat. "
            "Oryx dig depressions in the ground with their front hooves to lie in cooler sand, providing protection "
            "against fierce desert winds. These animals seem able to detect rainfall a great distance away and live "
            "an almost nomadic life, traveling vast areas in search of new growth after intermittent rains. "
            "Their remarkable desert adaptations include reducing urine volume and resting metabolic rate by at least 50%."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_oryx",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Arabian_oryx_%28oryx_leucoryx%29.jpg/500px-Arabian_oryx_%28oryx_leucoryx%29.jpg",
        "provinces": ["riyadh", "eastern", "najran"],
    }
    return render(request, "main/arabian_oryx.html", {"species": species})


def sand_cat_view(request):
    species = {
        "slug": "sand-cat",
        "name": "Sand Cat",
        "scientific_name": "Felis margarita",
        "class": "mammals",
        "short_description": (
            "The only wild cat living primarily in true desert, perfectly adapted "
            "to extreme heat, cold nights, and scarce water. With thickly furred paws "
            "and enormous ears, the sand cat is built for survival in some of Earth's harshest landscapes."
        ),
        "habits_lifestyle": (
            "The sand cat is solitary except during mating and kitten-rearing, resting in underground dens "
            "during the day and hunting at night, traveling an average of 5.4 km nightly. It hunts small rodents, "
            "birds, and even venomous snakes with a sprint capability of 30–40 km/hour. Their large ears allow them "
            "to detect the faint vibrations of prey moving underground. Thickly furred paws protect them from "
            "scorching sand surfaces and enable near-silent movement while hunting. Females bear 2–3 kittens "
            "after a 59–66 day gestation, with young growing to near full size within just five months."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sand_cat",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Persian_sand_CAT.jpg/500px-Persian_sand_CAT.jpg",
        "provinces": ["riyadh", "eastern", "northern borders"],
    }
    return render(request, "main/sand_cat.html", {"species": species})


def arabian_leopard_view(request):
    species = {
        "slug": "arabian-leopard",
        "name": "Arabian Leopard",
        "scientific_name": "Panthera pardus nimr",
        "class": "mammals",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_leopard",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/arabian_leopard.html", {"species": species})


def nubian_ibex_view(request):
    species = {
        "slug": "nubian-ibex",
        "name": "Nubian Ibex",
        "scientific_name": "Capra nubiana",
        "class": "mammals",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Nubian_ibex",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/nubian_ibex.html", {"species": species})


def golden_eagle_view(request):
    species = {
        "slug": "golden-eagle",
        "name": "Golden Eagle",
        "scientific_name": "Aquila chrysaetos",
        "class": "birds",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Golden_eagle",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/golden_eagle.html", {"species": species})


def saker_falcon_view(request):
    species = {
        "slug": "saker-falcon",
        "name": "Saker Falcon",
        "scientific_name": "Falco cherrug",
        "class": "birds",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Saker_falcon",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/saker_falcon.html", {"species": species})


def spinner_dolphin_view(request):
    species = {
        "slug": "spinner-dolphin",
        "name": "Spinner Dolphin",
        "scientific_name": "Stenella longirostris",
        "class": "marine",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spinner_dolphin",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/spinner_dolphin.html", {"species": species})


def hamadryas_baboon_view(request):
    species = {
        "slug": "hamadryas-baboon",
        "name": "Hamadryas Baboon",
        "scientific_name": "Papio hamadryas",
        "class": "mammals",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Hamadryas_baboon",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/hamadryas_baboon.html", {"species": species})


def arabian_sand_boa_view(request):
    species = {
        "slug": "arabian-sand-boa",
        "name": "Arabian Sand Boa",
        "scientific_name": "Eryx jayakari",
        "class": "reptiles",
        "short_description": "",
        "habits_lifestyle": "",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Jayakar%27s_sand_boa",
        "image": "",
        "provinces": [],
    }
    return render(request, "main/arabian_sand_boa.html", {"species": species})


def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)
