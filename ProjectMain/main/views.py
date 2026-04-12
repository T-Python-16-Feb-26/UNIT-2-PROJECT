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
        "image": "https://s3.animalia.bio/animals/photos/full/original/pikiwiki-israel-21618-leopard-in-the-judean-desert-photographed-byjpg.webp",
        "provinces": [],
    }
    return render(request, "main/arabian_leopard.html", {"species": species})


def nubian_ibex_view(request):
    species = {
        "slug": "nubian-ibex",
        "name": "Nubian Ibex",
        "scientific_name": "Capra nubiana",
        "class": "mammals",
        "short_description": (
            "A sure-footed wild goat that inhabits the rocky escarpments and wadis "
            "of southwestern Saudi Arabia, the male's swept-back horns are iconic."
        ),
        "habits_lifestyle": "Nubian ibexes are very agile and hardy animals that can climb on bare rock with ease, accessing terrain that would be dangerous for most other animals. Males and females live separately for most of the year, coming together only during the rut. They are most active in the morning and evening, resting in shaded spots during the heat of the day. Their strong hind legs serve both for climbing and as a defence against predators. An interesting feature of their ecology is their relationship with grackles, which are often seen on ibex backs searching for insects. When Nubian ibexes dig shallow resting depressions in the soil, these create microhabitats where a diverse range of seedlings can germinate, adding to the biodiversity of their habitat.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Nubian_ibex",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/PikiWiki_Israel_38769_Male_Ibex.jpg/500px-PikiWiki_Israel_38769_Male_Ibex.jpg",
        "provinces": ["asir", "tabuk", "hail"],
    }
    return render(request, "main/nubian_ibex.html", {"species": species})


def golden_eagle_view(request):
    species = {
        "slug": "golden-eagle",
        "name": "Golden Eagle",
        "scientific_name": "Aquila chrysaetos",
        "class": "birds",
        "short_description": (
            "One of the most powerful raptors on Earth, soaring on broad wings "
            "over mountain ranges and hunting hares and other large prey."
        ),
        "habits_lifestyle": "Golden eagles are diurnal raptors, active by day and roosting at night. They usually live alone or in bonded pairs, soaring over vast territories in mountainous areas, though they also inhabit grasslands, shrublands, and tundra. They avoid heavily forested regions and developed land. Most populations are sedentary but the species is a partial migrant, with northernmost birds moving south in autumn. Golden eagles hunt by stooping at high speed on mammals such as hares and rabbits, and will also take birds and carrion. They hold large territories and use the same nest sites — called eyries — for years, adding material each season.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Golden_eagle",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/015_Wild_Golden_Eagle_in_flight_at_Pfyn-Finges_%28Switzerland%29_Photo_by_Giles_Laurent.jpg/500px-015_Wild_Golden_Eagle_in_flight_at_Pfyn-Finges_%28Switzerland%29_Photo_by_Giles_Laurent.jpg",
        "provinces": ["asir", "tabuk", "hail"],
    }
    return render(request, "main/golden_eagle.html", {"species": species})


def saker_falcon_view(request):
    species = {
        "slug": "saker-falcon",
        "name": "Saker Falcon",
        "scientific_name": "Falco cherrug",
        "class": "birds",
        "short_description": (
            "Prized across the Arabian world for falconry, the powerful Saker is "
            "an endangered species whose wild populations face ongoing pressure."
        ),
        "habits_lifestyle":"Saker falcons are active during the day and spend most of their time hunting. They often hunt by horizontal pursuit and usually close to the ground. They are very patient hunters soaring in the air or sitting on the perch for hours watching for prey; when the prey is spotted they suddenly dive for the kill. Saker falcons are not very social birds and are usually seen alone or in pairs; breeding pairs prefer to nest solitary, however, in areas where food is plentiful, Saker falcons may nest closer to each other. Saker falcons communicate vocally and their call is a sharp 'kiy-ee' or a repeated 'kyak-kyak-kyak'.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Saker_falcon",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Falco_cherrug_%28Marek_Szczepanek%29.jpg/500px-Falco_cherrug_%28Marek_Szczepanek%29.jpg",
        "provinces": ["riyadh", "eastern-province", "tabuk", "hail"],
    }
    return render(request, "main/saker_falcon.html", {"species": species})


def spinner_dolphin_view(request):
    species = {
        "slug": "spinner-dolphin",
        "name": "Spinner Dolphin",
        "scientific_name": "Stenella longirostris",
        "class": "mammals",
        "short_description": (
            "Famous for its acrobatic leaping spins above the water surface, "
            "this sociable dolphin frequents the Red Sea and Arabian Gulf."
        ),
        "habits_lifestyle": "Spinner dolphins are highly social animals, gathering in groups that range from just a few individuals to over a thousand. During the day they typically rest in sheltered inlets, often returning to the same locations each day. At sunset they move offshore to feed, and it is during these nighttime hours that they perform their famous acrobatic spins and leaps. They are migratory, travelling long distances to follow prey and to stay within warm waters. Communication relies on echolocation — a sophisticated biological sonar — as well as touch, which plays an important role in maintaining social bonds within the group.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spinner_dolphin",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Gray%27s_spinner_dolphin_%28Stenella_longirostris_longirostris%29_Panglao.jpg",
        "provinces": ["makkah", "jizan", "eastern-province"],
    }
    return render(request, "main/spinner_dolphin.html", {"species": species})


def hamadryas_baboon_view(request):
    species = {
        "slug": "hamadryas-baboon",
        "name": "Hamadryas Baboon",
        "scientific_name": "Papio hamadryas",
        "class": "mammals",
        "short_description": (
            "Large, highly social primates that form troops of hundreds in the "
            "rocky hillsides and gorges of the Asir and Jizan regions."
        ),
        "habits_lifestyle": "Hamadryas baboons are diurnal animals, active during the day and sleeping at night on cliff faces or in trees that offer protection from predators. Their basic social unit is the one-male unit (OMU), consisting of a dominant male, several females, and their young. Several OMUs may band together into groups of 30 to 90 individuals, and multiple bands can converge at sleeping cliffs to form troops of several hundred. Group members engage in collective activities including foraging, travelling, and grooming, the latter being an important social activity that reinforces bonds. Hamadryas baboons are omnivores, eating fruits, seeds, roots, tubers, insects, and occasionally small vertebrates. They always remain close to water sources, and some populations move to mountain areas during the wet season.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Hamadryas_baboon",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Papio_hamadryas_pair.jpg/500px-Papio_hamadryas_pair.jpg",
        "provinces": ["asir", "jizan", "bahah"],
    }
    return render(request, "main/hamadryas_baboon.html", {"species": species})


def arabian_sand_boa_view(request):
    species = {
        "slug": "arabian-sand-boa",
        "name": "Arabian Sand Boa",
        "scientific_name": "Eryx jayakari",
        "class": "reptiles",
        "short_description": (
            "A small, blunt-headed burrowing snake that hunts lizards and rodents "
            "beneath the sand surface, perfectly camouflaged in the desert."
        ),
        "habits_lifestyle": "Arabian sand boas are nocturnal and spend the day buried beneath loose desert sand, emerging at night to hunt. They are endemic to the Arabian Peninsula and Iran. Their burrowing lifestyle gives them excellent insulation from daytime heat while keeping them concealed from predators. Like other sand boas they are constrictors, subduing small lizards and rodents by coiling around them. Their blunt, upturned snout and smooth scales are adaptations for sand-diving. They are solitary reptiles that rely entirely on ambush rather than active pursuit to catch prey.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Jayakar%27s_sand_boa",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Eryx_jayakari_by_Omid_Mozaffari.jpg",
        "provinces": ["riyadh", "eastern-province", "hail"],
    }
    return render(request, "main/arabian_sand_boa.html", {"species": species})


def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)
