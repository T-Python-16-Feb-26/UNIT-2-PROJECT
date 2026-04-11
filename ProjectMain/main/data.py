# ─────────────────────────────────────────────────────────────
#  101 Wildlife Species of Saudi Arabia — Static Data
#  All 101 species organised by taxonomic class.
#  Featured species have additional data in FEATURED_EXTRA.
# ─────────────────────────────────────────────────────────────

SPECIES = {

    # ── MAMMALS ──────────────────────────────────────────────

    "arabian-oryx": {
        "slug": "arabian-oryx",
        "name": "Arabian Oryx",
        "scientific_name": "Oryx leucoryx",
        "class": "mammals",
        "short_description": (
            "The national animal of Saudi Arabia, reintroduced from near-extinction "
            "through dedicated conservation efforts across the Arabian Peninsula."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_oryx",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "najran"],
    },
    "arabian-gazelle": {
        "slug": "arabian-gazelle",
        "name": "Arabian Gazelle",
        "scientific_name": "Gazella arabica",
        "class": "mammals",
        "short_description": (
            "A slender, pale-coated gazelle native to the deserts and hills of "
            "the Arabian Peninsula, known for its remarkable speed and grace."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_gazelle",
        "image": None,
        "provinces": ["riyadh", "makkah", "asir"],
    },
    "nubian-ibex": {
        "slug": "nubian-ibex",
        "name": "Nubian Ibex",
        "scientific_name": "Capra nubiana",
        "class": "mammals",
        "short_description": (
            "A sure-footed wild goat that inhabits the rocky escarpments and wadis "
            "of southwestern Saudi Arabia, the male's swept-back horns are iconic."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Nubian_ibex",
        "image": None,
        "provinces": ["asir", "tabuk", "hail"],
    },
    "arabian-sand-gazelle": {
        "slug": "arabian-sand-gazelle",
        "name": "Arabian Sand Gazelle",
        "scientific_name": "Gazella subgutturosa marica",
        "class": "mammals",
        "short_description": (
            "Adapted to extreme aridity, this pale gazelle roams vast sand seas and "
            "gravel plains, surviving on sparse desert vegetation."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Rhim_gazelle",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "northern-borders"],
    },
    "arabian-leopard": {
        "slug": "arabian-leopard",
        "name": "Arabian Leopard",
        "scientific_name": "Panthera pardus nimr",
        "class": "mammals",
        "short_description": (
            "The rarest of all leopard subspecies, critically endangered and clinging "
            "to survival in the rugged mountains of Asir and Hejaz."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_leopard",
        "image": None,
        "provinces": ["asir", "jizan", "makkah"],
    },
    "caracal": {
        "slug": "caracal",
        "name": "Caracal",
        "scientific_name": "Caracal caracal",
        "class": "mammals",
        "short_description": (
            "A medium-sized wild cat famed for its distinctive tufted ears and "
            "extraordinary leaping ability when hunting birds mid-flight."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caracal",
        "image": None,
        "provinces": ["asir", "makkah", "riyadh"],
    },
    "sand-cat": {
        "slug": "sand-cat",
        "name": "Sand Cat",
        "scientific_name": "Felis margarita",
        "class": "mammals",
        "short_description": (
            "The world's only true desert cat, with thickly furred paws that act "
            "as natural snowshoes on the scorching sand."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sand_cat",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "arabian-red-fox": {
        "slug": "arabian-red-fox",
        "name": "Arabian Red Fox",
        "scientific_name": "Vulpes vulpes arabica",
        "class": "mammals",
        "short_description": (
            "A smaller, paler subspecies of the red fox adapted to the heat of "
            "the Arabian Peninsula, highly opportunistic and widespread."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Red_fox",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "makkah", "asir"],
    },
    "arabian-wolf": {
        "slug": "arabian-wolf",
        "name": "Arabian Wolf",
        "scientific_name": "Canis lupus arabs",
        "class": "mammals",
        "short_description": (
            "The smallest wolf subspecies, lean and long-legged, it roams remote "
            "mountain and desert regions in small family groups."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_wolf",
        "image": None,
        "provinces": ["asir", "najran", "jizan"],
    },
    "desert-hedgehog": {
        "slug": "desert-hedgehog",
        "name": "Desert Hedgehog",
        "scientific_name": "Paraechinus aethiopicus",
        "class": "mammals",
        "short_description": (
            "The smallest hedgehog in the world, this nocturnal insectivore thrives "
            "in sandy desert habitats across the Arabian Peninsula."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Desert_hedgehog",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail","mecca"],
    },
    "brandts-hedgehog": {
        "slug": "brandts-hedgehog",
        "name": "Brandt's Hedgehog",
        "scientific_name": "Paraechinus hypomelas",
        "class": "mammals",
        "short_description": (
            "A large, dark-spined hedgehog found in rocky and arid terrain, "
            "distinguished from other hedgehogs by its black-tipped quills."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Brandt%27s_hedgehog",
        "image": None,
        "provinces": ["tabuk", "hail", "jouf"],
    },
    "spinner-dolphin": {
        "slug": "spinner-dolphin",
        "name": "Spinner Dolphin",
        "scientific_name": "Stenella longirostris",
        "class": "mammals",
        "short_description": (
            "Famous for its acrobatic leaping spins above the water surface, "
            "this sociable dolphin frequents the Red Sea and Arabian Gulf."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spinner_dolphin",
        "image": None,
        "provinces": ["makkah", "jizan", "eastern-province"],
    },
    "common-bottlenose-dolphin": {
        "slug": "common-bottlenose-dolphin",
        "name": "Common Bottlenose Dolphin",
        "scientific_name": "Tursiops truncatus",
        "class": "mammals",
        "short_description": (
            "The most widely recognised dolphin species, highly intelligent and "
            "found in both the Red Sea and the Arabian Gulf."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Common_bottlenose_dolphin",
        "image": None,
        "provinces": ["makkah", "eastern-province"],
    },
    "dugong": {
        "slug": "dugong",
        "name": "Dugong",
        "scientific_name": "Dugong dugon",
        "class": "mammals",
        "short_description": (
            "A gentle marine herbivore and the only living species of its family, "
            "grazing on seagrass beds in the warm waters of the Arabian Gulf."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Dugong",
        "image": None,
        "provinces": ["eastern-province"],
    },
    "hamadryas-baboon": {
        "slug": "hamadryas-baboon",
        "name": "Hamadryas Baboon",
        "scientific_name": "Papio hamadryas",
        "class": "mammals",
        "short_description": (
            "Large, highly social primates that form troops of hundreds in the "
            "rocky hillsides and gorges of the Asir and Jizan regions."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Hamadryas_baboon",
        "image": None,
        "provinces": ["asir", "jizan", "bahah"],
    },
    "arabian-jird": {
        "slug": "arabian-jird",
        "name": "Arabian Jird",
        "scientific_name": "Meriones crassus",
        "class": "mammals",
        "short_description": (
            "A large gerbil-like rodent that builds extensive burrow systems in "
            "sandy and gravelly desert soils across the peninsula."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sundevall%27s_jird",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail"],
    },
    "cheesmans-gerbil": {
        "slug": "cheesmans-gerbil",
        "name": "Cheesman's Gerbil",
        "scientific_name": "Gerbillus cheesmani",
        "class": "mammals",
        "short_description": (
            "A small, sand-coloured nocturnal rodent that hops on enlarged hind "
            "legs across the bare sand seas of the Arabian interior."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Cheesman%27s_gerbil",
        "image": None,
        "provinces": ["riyadh", "eastern-province"],
    },
    "lesser-egyptian-jerboa": {
        "slug": "lesser-egyptian-jerboa",
        "name": "Lesser Egyptian Jerboa",
        "scientific_name": "Jaculus jaculus",
        "class": "mammals",
        "short_description": (
            "A tiny desert rodent with extraordinarily long hind legs that allow "
            "it to cover ground in long bounding leaps to escape predators."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Lesser_Egyptian_jerboa",
        "image": None,
        "provinces": ["riyadh", "tabuk", "northern-borders"],
    },
    "cape-hare": {
        "slug": "cape-hare",
        "name": "Cape Hare",
        "scientific_name": "Lepus capensis",
        "class": "mammals",
        "short_description": (
            "A widespread and adaptable hare found across diverse Saudi habitats "
            "from coastal plains to high-altitude mountain grasslands."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Cape_hare",
        "image": None,
        "provinces": ["riyadh", "makkah", "asir", "tabuk"],
    },
    "rock-hyrax": {
        "slug": "rock-hyrax",
        "name": "Rock Hyrax",
        "scientific_name": "Procavia capensis",
        "class": "mammals",
        "short_description": (
            "Deceptively related to elephants, these compact, rabbit-like mammals "
            "live in rock colonies on the escarpments of southwestern Arabia."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Rock_hyrax",
        "image": None,
        "provinces": ["asir", "jizan", "makkah"],
    },
    "egyptian-fruit-bat": {
        "slug": "egyptian-fruit-bat",
        "name": "Egyptian Fruit Bat",
        "scientific_name": "Rousettus aegyptiacus",
        "class": "mammals",
        "short_description": (
            "The only Old World fruit bat to use echolocation, roosting in large "
            "colonies in caves and foraging on date palms and figs."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Egyptian_fruit_bat",
        "image": None,
        "provinces": ["makkah", "madinah", "asir"],
    },
    "fat-sand-rat": {
        "slug": "fat-sand-rat",
        "name": "Fat Sand Rat",
        "scientific_name": "Psammomys obesus",
        "class": "mammals",
        "short_description": (
            "A diurnal rodent that feeds almost exclusively on salt-laden succulent "
            "plants, thriving in the sabkha flats of the Eastern Province."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Fat_sand_rat",
        "image": None,
        "provinces": ["eastern-province", "riyadh"],
    },
    "common-genet": {
        "slug": "common-genet",
        "name": "Common Genet",
        "scientific_name": "Genetta genetta",
        "class": "mammals",
        "short_description": (
            "A slender, spotted carnivore resembling a cross between a cat and "
            "a weasel, nimble and nocturnal in dense vegetation."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Common_genet",
        "image": None,
        "provinces": ["asir", "jizan"],
    },
    "white-tailed-mongoose": {
        "slug": "white-tailed-mongoose",
        "name": "White-tailed Mongoose",
        "scientific_name": "Ichneumia albicauda",
        "class": "mammals",
        "short_description": (
            "The largest African mongoose, recognisable by its bushy white tail, "
            "found in the moist wadis and forested slopes of Asir."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White-tailed_mongoose",
        "image": None,
        "provinces": ["asir", "jizan", "bahah"],
    },

    # ── BIRDS ────────────────────────────────────────────────

    "greater-flamingo": {
        "slug": "greater-flamingo",
        "name": "Greater Flamingo",
        "scientific_name": "Phoenicopterus roseus",
        "class": "birds",
        "short_description": (
            "The largest flamingo species, flocking in thousands on shallow coastal "
            "lagoons and salt lakes, its pink plumage derived from its diet."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Greater_flamingo",
        "image": None,
        "provinces": ["eastern-province", "jizan", "makkah"],
    },
    "lesser-flamingo": {
        "slug": "lesser-flamingo",
        "name": "Lesser Flamingo",
        "scientific_name": "Phoeniconaias minor",
        "class": "birds",
        "short_description": (
            "The smallest and most numerous flamingo, filtering blue-green algae "
            "from alkaline lakes with its uniquely keeled bill."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Lesser_flamingo",
        "image": None,
        "provinces": ["eastern-province", "jizan"],
    },
    "great-egret": {
        "slug": "great-egret",
        "name": "Great Egret",
        "scientific_name": "Ardea alba",
        "class": "birds",
        "short_description": (
            "A tall, all-white heron found along waterways and wetlands, hunting "
            "fish with slow deliberate strides before a lightning-fast strike."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Great_egret",
        "image": None,
        "provinces": ["eastern-province", "makkah", "jizan"],
    },
    "grey-heron": {
        "slug": "grey-heron",
        "name": "Grey Heron",
        "scientific_name": "Ardea cinerea",
        "class": "birds",
        "short_description": (
            "Europe and Asia's largest heron, a patient riverside fisherman that "
            "stands motionless for long periods before striking at prey."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Grey_heron",
        "image": None,
        "provinces": ["eastern-province", "makkah", "madinah"],
    },
    "mallard": {
        "slug": "mallard",
        "name": "Mallard",
        "scientific_name": "Anas platyrhynchos",
        "class": "birds",
        "short_description": (
            "The ancestor of most domestic duck breeds, the male's iridescent green "
            "head makes it one of the world's most recognisable waterbirds."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Mallard",
        "image": None,
        "provinces": ["eastern-province", "tabuk"],
    },
    "ruddy-shelduck": {
        "slug": "ruddy-shelduck",
        "name": "Ruddy Shelduck",
        "scientific_name": "Tadorna ferruginea",
        "class": "birds",
        "short_description": (
            "A striking orange-chestnut duck that winters on freshwater lakes and "
            "slow rivers, often seen in pairs or small flocks."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Ruddy_shelduck",
        "image": None,
        "provinces": ["eastern-province", "tabuk", "jouf"],
    },
    "eurasian-teal": {
        "slug": "eurasian-teal",
        "name": "Eurasian Teal",
        "scientific_name": "Anas crecca",
        "class": "birds",
        "short_description": (
            "One of the smallest dabbling ducks, wintering in large flocks on "
            "wetlands and coastal lagoons across the Arabian Peninsula."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Eurasian_teal",
        "image": None,
        "provinces": ["eastern-province", "jizan"],
    },
    "rock-dove": {
        "slug": "rock-dove",
        "name": "Rock Dove",
        "scientific_name": "Columba livia",
        "class": "birds",
        "short_description": (
            "The wild ancestor of all domestic pigeons, nesting on cliff faces and "
            "buildings, adaptable to both wilderness and urban environments."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Rock_dove",
        "image": None,
        "provinces": ["riyadh", "makkah", "madinah", "asir"],
    },
    "laughing-dove": {
        "slug": "laughing-dove",
        "name": "Laughing Dove",
        "scientific_name": "Spilopelia senegalensis",
        "class": "birds",
        "short_description": (
            "A small, pinkish-brown dove named for its soft bubbling call, one "
            "of the most common and familiar birds in Saudi towns and gardens."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Laughing_dove",
        "image": None,
        "provinces": ["riyadh", "makkah", "madinah", "jizan"],
    },
    "golden-eagle": {
        "slug": "golden-eagle",
        "name": "Golden Eagle",
        "scientific_name": "Aquila chrysaetos",
        "class": "birds",
        "short_description": (
            "One of the most powerful raptors on Earth, soaring on broad wings "
            "over mountain ranges and hunting hares and other large prey."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Golden_eagle",
        "image": None,
        "provinces": ["asir", "tabuk", "hail"],
    },
    "black-kite": {
        "slug": "black-kite",
        "name": "Black Kite",
        "scientific_name": "Milvus migrans",
        "class": "birds",
        "short_description": (
            "An opportunistic and highly social raptor that gathers in large numbers "
            "around refuse tips, markets, and fishing harbours."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Black_kite",
        "image": None,
        "provinces": ["riyadh", "makkah", "jizan", "eastern-province"],
    },
    "black-winged-kite": {
        "slug": "black-winged-kite",
        "name": "Black-winged Kite",
        "scientific_name": "Elanus caeruleus",
        "class": "birds",
        "short_description": (
            "A small, ghostly pale raptor with striking red eyes that hovers "
            "kestrel-like over open grassland before dropping on small rodents."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Black-winged_kite",
        "image": None,
        "provinces": ["asir", "jizan", "makkah"],
    },
    "white-tailed-eagle": {
        "slug": "white-tailed-eagle",
        "name": "White-tailed Eagle",
        "scientific_name": "Haliaeetus albicilla",
        "class": "birds",
        "short_description": (
            "Europe's largest eagle, a scarce winter visitor to Saudi Arabia's "
            "large lakes and coastal wetlands, recognised by its pale wedge tail."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White-tailed_eagle",
        "image": None,
        "provinces": ["eastern-province", "tabuk"],
    },
    "eastern-imperial-eagle": {
        "slug": "eastern-imperial-eagle",
        "name": "Eastern Imperial Eagle",
        "scientific_name": "Aquila heliaca",
        "class": "birds",
        "short_description": (
            "A rare and majestic eagle that passes through Saudi Arabia on migration, "
            "identifiable by large white shoulder patches on dark plumage."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Eastern_imperial_eagle",
        "image": None,
        "provinces": ["eastern-province", "riyadh"],
    },
    "common-buzzard": {
        "slug": "common-buzzard",
        "name": "Common Buzzard",
        "scientific_name": "Buteo buteo",
        "class": "birds",
        "short_description": (
            "A highly variable medium-sized raptor that winters in open habitats "
            "across Saudi Arabia, often perching on telegraph poles."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Common_buzzard",
        "image": None,
        "provinces": ["riyadh", "tabuk", "asir"],
    },
    "egyptian-nightjar": {
        "slug": "egyptian-nightjar",
        "name": "Egyptian Nightjar",
        "scientific_name": "Caprimulgus aegyptius",
        "class": "birds",
        "short_description": (
            "A cryptically patterned nocturnal bird that roosts motionless on "
            "sandy desert ground by day, invisible against the substrate."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Egyptian_nightjar",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "white-stork": {
        "slug": "white-stork",
        "name": "White Stork",
        "scientific_name": "Ciconia ciconia",
        "class": "birds",
        "short_description": (
            "A large migratory bird that passes over Saudi Arabia in spectacular "
            "thermals of thousands on its journey between Europe and Africa."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White_stork",
        "image": None,
        "provinces": ["riyadh", "makkah", "eastern-province"],
    },
    "black-stork": {
        "slug": "black-stork",
        "name": "Black Stork",
        "scientific_name": "Ciconia nigra",
        "class": "birds",
        "short_description": (
            "A shy and secretive stork with iridescent black-green plumage, "
            "favouring forest rivers on its long migration south."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Black_stork",
        "image": None,
        "provinces": ["tabuk", "makkah"],
    },
    "yellow-legged-gull": {
        "slug": "yellow-legged-gull",
        "name": "Yellow-legged Gull",
        "scientific_name": "Larus michahellis",
        "class": "birds",
        "short_description": (
            "A large white-headed gull with bright yellow legs, common along "
            "the Red Sea coast and around fishing ports."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Yellow-legged_gull",
        "image": None,
        "provinces": ["makkah", "jizan", "eastern-province"],
    },
    "lesser-black-backed-gull": {
        "slug": "lesser-black-backed-gull",
        "name": "Lesser Black-backed Gull",
        "scientific_name": "Larus fuscus",
        "class": "birds",
        "short_description": (
            "A migratory gull with slate-grey upperparts and yellow legs, "
            "wintering in large numbers along Saudi coasts and inland lakes."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Lesser_black-backed_gull",
        "image": None,
        "provinces": ["eastern-province", "makkah"],
    },
    "white-wagtail": {
        "slug": "white-wagtail",
        "name": "White Wagtail",
        "scientific_name": "Motacilla alba",
        "class": "birds",
        "short_description": (
            "A trim black-and-white bird with a constantly bobbing tail, "
            "common in open habitats near water throughout the Kingdom."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White_wagtail",
        "image": None,
        "provinces": ["riyadh", "madinah", "asir"],
    },
    "eurasian-hoopoe": {
        "slug": "eurasian-hoopoe",
        "name": "Eurasian Hoopoe",
        "scientific_name": "Upupa epops",
        "class": "birds",
        "short_description": (
            "With its cinnamon plumage and dramatic black-tipped fan crest, "
            "the hoopoe is one of the Kingdom's most striking resident birds."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Eurasian_hoopoe",
        "image": None,
        "provinces": ["riyadh", "makkah", "asir", "madinah"],
    },
    "long-eared-owl": {
        "slug": "long-eared-owl",
        "name": "Long-eared Owl",
        "scientific_name": "Asio otus",
        "class": "birds",
        "short_description": (
            "A slender owl named for its prominent ear tufts that roosts "
            "communally in dense thickets during winter migration."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Long-eared_owl",
        "image": None,
        "provinces": ["tabuk", "hail", "madinah"],
    },
    "short-eared-owl": {
        "slug": "short-eared-owl",
        "name": "Short-eared Owl",
        "scientific_name": "Asio flammeus",
        "class": "birds",
        "short_description": (
            "One of the world's most widespread owls, this grassland hunter is "
            "often seen quartering open desert by day in winter."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Short-eared_owl",
        "image": None,
        "provinces": ["eastern-province", "riyadh", "tabuk"],
    },
    "common-moorhen": {
        "slug": "common-moorhen",
        "name": "Common Moorhen",
        "scientific_name": "Gallinula chloropus",
        "class": "birds",
        "short_description": (
            "A secretive wetland bird with a bright red-and-yellow bill shield, "
            "jerking its head as it swims or picks food at the water's edge."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Common_moorhen",
        "image": None,
        "provinces": ["eastern-province", "asir", "jizan"],
    },
    "jacobin-cuckoo": {
        "slug": "jacobin-cuckoo",
        "name": "Jacobin Cuckoo",
        "scientific_name": "Clamator jacobinus",
        "class": "birds",
        "short_description": (
            "A bold black-and-white cuckoo associated with the onset of seasonal "
            "rains in tropical Africa and the southern Arabian Peninsula."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Jacobin_cuckoo",
        "image": None,
        "provinces": ["jizan", "asir"],
    },
    "saker-falcon": {
        "slug": "saker-falcon",
        "name": "Saker Falcon",
        "scientific_name": "Falco cherrug",
        "class": "birds",
        "short_description": (
            "Prized across the Arabian world for falconry, the powerful Saker is "
            "an endangered species whose wild populations face ongoing pressure."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Saker_falcon",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk", "hail"],
    },
    "steppe-eagle": {
        "slug": "steppe-eagle",
        "name": "Steppe Eagle",
        "scientific_name": "Aquila nipalensis",
        "class": "birds",
        "short_description": (
            "A large dark eagle that migrates in enormous numbers through Saudi "
            "Arabia, gathering at thermals over mountain ridges."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Steppe_eagle",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "grey-wagtail": {
        "slug": "grey-wagtail",
        "name": "Grey Wagtail",
        "scientific_name": "Motacilla cinerea",
        "class": "birds",
        "short_description": (
            "A long-tailed wagtail with grey upperparts and bright yellow underparts, "
            "always found near fast-flowing streams and rocky rivers."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Grey_wagtail",
        "image": None,
        "provinces": ["asir", "jizan", "bahah"],
    },
    "western-yellow-wagtail": {
        "slug": "western-yellow-wagtail",
        "name": "Western Yellow Wagtail",
        "scientific_name": "Motacilla flava",
        "class": "birds",
        "short_description": (
            "A slim, bright-yellow wagtail that winters abundantly in cultivation "
            "and moist areas, often following cattle for flushed insects."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Western_yellow_wagtail",
        "image": None,
        "provinces": ["eastern-province", "jizan", "riyadh"],
    },
    "eurasian-curlew": {
        "slug": "eurasian-curlew",
        "name": "Eurasian Curlew",
        "scientific_name": "Numenius arquata",
        "class": "birds",
        "short_description": (
            "Europe's largest wader, recognised by its enormously long, down-curved "
            "bill used to probe mud and sand for invertebrates."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Eurasian_curlew",
        "image": None,
        "provinces": ["eastern-province", "makkah"],
    },
    "lesser-kestrel": {
        "slug": "lesser-kestrel",
        "name": "Lesser Kestrel",
        "scientific_name": "Falco naumanni",
        "class": "birds",
        "short_description": (
            "A colonial falcon that migrates through in large flocks, hovering "
            "over open fields to spot grasshoppers and other invertebrates."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Lesser_kestrel",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "spotted-eagle-owl": {
        "slug": "spotted-eagle-owl",
        "name": "Spotted Eagle-Owl",
        "scientific_name": "Bubo africanus",
        "class": "birds",
        "short_description": (
            "A medium-sized eagle-owl with prominent ear tufts and yellow eyes, "
            "hunting insects and small vertebrates in rocky hillsides."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spotted_eagle-owl",
        "image": None,
        "provinces": ["asir", "jizan", "bahah"],
    },
    "african-hoopoe": {
        "slug": "african-hoopoe",
        "name": "African Hoopoe",
        "scientific_name": "Upupa africana",
        "class": "birds",
        "short_description": (
            "Similar to the Eurasian Hoopoe but with a fully rufous crest, "
            "this southern species reaches the southwestern tip of the Kingdom."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/African_hoopoe",
        "image": None,
        "provinces": ["jizan", "asir"],
    },
    "white-eared-bulbul": {
        "slug": "white-eared-bulbul",
        "name": "White-eared Bulbul",
        "scientific_name": "Pycnonotus leucotis",
        "class": "birds",
        "short_description": (
            "A lively, vocal bulbul with distinctive white cheek patches and a "
            "yellow vent, common in gardens and date palm groves."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White-eared_bulbul",
        "image": None,
        "provinces": ["eastern-province", "riyadh"],
    },
    "house-sparrow": {
        "slug": "house-sparrow",
        "name": "House Sparrow",
        "scientific_name": "Passer domesticus",
        "class": "birds",
        "short_description": (
            "Humanity's most faithful avian companion, nesting in every city, "
            "town, and village across the Kingdom and almost every nation on Earth."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/House_sparrow",
        "image": None,
        "provinces": ["riyadh", "makkah", "madinah", "eastern-province"],
    },
    "barn-owl": {
        "slug": "barn-owl",
        "name": "Barn Owl",
        "scientific_name": "Tyto alba",
        "class": "birds",
        "short_description": (
            "The world's most widespread land bird, with a heart-shaped facial "
            "disc that focuses sound to hunt rodents in total darkness."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Barn_owl",
        "image": None,
        "provinces": ["riyadh", "makkah", "asir", "eastern-province"],
    },
    "little-owl": {
        "slug": "little-owl",
        "name": "Little Owl",
        "scientific_name": "Athene noctua",
        "class": "birds",
        "short_description": (
            "A tiny, flat-headed owl with bold yellow eyes that bobs up and down "
            "when alarmed, active at dawn and dusk in open dry habitats."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Little_owl",
        "image": None,
        "provinces": ["riyadh", "tabuk", "hail"],
    },
    "pharaoh-eagle-owl": {
        "slug": "pharaoh-eagle-owl",
        "name": "Pharaoh Eagle-Owl",
        "scientific_name": "Bubo ascalaphus",
        "class": "birds",
        "short_description": (
            "A large, tawny-coloured eagle-owl of the Middle Eastern deserts, "
            "nesting among boulders and cliff faces in remote wadis."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Pharaoh_eagle-owl",
        "image": None,
        "provinces": ["riyadh", "tabuk", "hail", "jouf"],
    },
    "desert-owl": {
        "slug": "desert-owl",
        "name": "Desert Owl",
        "scientific_name": "Strix hadorami",
        "class": "birds",
        "short_description": (
            "A recently described owl species endemic to the Middle East, found "
            "in rocky wadis and sparse woodland of Arabia."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Desert_owl",
        "image": None,
        "provinces": ["riyadh", "makkah", "madinah"],
    },
    "white-spectacled-bulbul": {
        "slug": "white-spectacled-bulbul",
        "name": "White-spectacled Bulbul",
        "scientific_name": "Pycnonotus xanthopygos",
        "class": "birds",
        "short_description": (
            "A noisy, sociable bulbul with a white eye-ring and yellow undertail "
            "coverts, common in gardens, orchards, and scrub."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/White-spectacled_bulbul",
        "image": None,
        "provinces": ["makkah", "madinah", "asir"],
    },
    "asir-magpie": {
        "slug": "asir-magpie",
        "name": "Asir Magpie",
        "scientific_name": "Pica asirensis",
        "class": "birds",
        "short_description": (
            "A critically endangered magpie found only in the high-altitude juniper "
            "forests of the Asir Mountains, unique to Saudi Arabia."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Asir_magpie",
        "image": None,
        "provinces": ["asir"],
    },
    "sandgrouse": {
        "slug": "sandgrouse",
        "name": "Spotted Sandgrouse",
        "scientific_name": "Pterocles senegallus",
        "class": "birds",
        "short_description": (
            "A fast-flying desert bird that gathers at water holes at dawn, "
            "the male soaking breast feathers to transport water to chicks."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spotted_sandgrouse",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail", "tabuk"],
    },
    "arabian-babbler": {
        "slug": "arabian-babbler",
        "name": "Arabian Babbler",
        "scientific_name": "Turdoides squamiceps",
        "class": "birds",
        "short_description": (
            "A cooperative breeder living in noisy groups, studying these "
            "long-lived birds has provided key insights into altruistic behaviour."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_babbler",
        "image": None,
        "provinces": ["madinah", "tabuk", "hail"],
    },
    "trumpeter-finch": {
        "slug": "trumpeter-finch",
        "name": "Trumpeter Finch",
        "scientific_name": "Bucanetes githagineus",
        "class": "birds",
        "short_description": (
            "A small, stout-billed finch of rocky desert terrain, named for its "
            "nasal, toy-trumpet-like call heard among boulders and gravel."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Trumpeter_finch",
        "image": None,
        "provinces": ["tabuk", "hail", "madinah"],
    },
    "desert-lark": {
        "slug": "desert-lark",
        "name": "Desert Lark",
        "scientific_name": "Ammomanes deserti",
        "class": "birds",
        "short_description": (
            "A sandy-coloured lark that perfectly matches its rocky desert habitat, "
            "singing a simple but melodious song from a prominent stone."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Desert_lark",
        "image": None,
        "provinces": ["riyadh", "tabuk", "hail", "jouf"],
    },
    "desert-finch": {
        "slug": "desert-finch",
        "name": "Desert Finch",
        "scientific_name": "Rhodospiza obsoleta",
        "class": "birds",
        "short_description": (
            "A pale finch of arid scrub with a striking black-and-white wing "
            "pattern, often visiting gardens and orchards for seeds."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Desert_finch",
        "image": None,
        "provinces": ["tabuk", "madinah", "hail"],
    },
    "crowned-sandgrouse": {
        "slug": "crowned-sandgrouse",
        "name": "Crowned Sandgrouse",
        "scientific_name": "Pterocles coronatus",
        "class": "birds",
        "short_description": (
            "A beautifully patterned sandgrouse of stony desert and ergs, "
            "gathering in flocks at desert waterholes around dawn."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Crowned_sandgrouse",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "arabian-wheatear": {
        "slug": "arabian-wheatear",
        "name": "Arabian Wheatear",
        "scientific_name": "Oenanthe lugentoides",
        "class": "birds",
        "short_description": (
            "A near-endemic wheatear of rocky hillsides in western Arabia, "
            "the male's contrasting black-and-white plumage is unmistakable."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_wheatear",
        "image": None,
        "provinces": ["asir", "makkah", "madinah"],
    },
    "arabian-golden-sparrow": {
        "slug": "arabian-golden-sparrow",
        "name": "Arabian Golden Sparrow",
        "scientific_name": "Passer euchlorus",
        "class": "birds",
        "short_description": (
            "The male is a dazzling yellow, one of the most colourful sparrows "
            "in the world, found in acacia scrub of the Tihama plain."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Arabian_golden_sparrow",
        "image": None,
        "provinces": ["jizan", "asir"],
    },
    "sinai-rosefinch": {
        "slug": "sinai-rosefinch",
        "name": "Sinai Rosefinch",
        "scientific_name": "Carpodacus synoicus",
        "class": "birds",
        "short_description": (
            "A rose-pink finch of high rocky deserts and granite mountains, "
            "Saudi Arabia's national bird and a true desert gem."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sinai_rosefinch",
        "image": None,
        "provinces": ["tabuk", "hail"],
    },
    "helmeted-guineafowl": {
        "slug": "helmeted-guineafowl",
        "name": "Helmeted Guineafowl",
        "scientific_name": "Numida meleagris",
        "class": "birds",
        "short_description": (
            "A gregarious ground bird introduced or naturalised in parts of "
            "southwestern Arabia, unmistakable with its bony blue head casque."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Helmeted_guineafowl",
        "image": None,
        "provinces": ["jizan", "asir"],
    },
    "tawny-eagle": {
        "slug": "tawny-eagle",
        "name": "Tawny Eagle",
        "scientific_name": "Aquila rapax",
        "class": "birds",
        "short_description": (
            "A large brown eagle that frequents open dry habitats and is known "
            "for kleptoparasitism, stealing prey from other raptors."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Tawny_eagle",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail"],
    },
    "pied-kingfisher": {
        "slug": "pied-kingfisher",
        "name": "Pied Kingfisher",
        "scientific_name": "Ceryle rudis",
        "class": "birds",
        "short_description": (
            "The world's largest hovering kingfisher, black and white, it "
            "plunge-dives from a stationary hover to catch fish."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Pied_kingfisher",
        "image": None,
        "provinces": ["eastern-province", "jizan", "asir"],
    },
    "spotted-thick-knee": {
        "slug": "spotted-thick-knee",
        "name": "Spotted Thick-knee",
        "scientific_name": "Burhinus capensis",
        "class": "birds",
        "short_description": (
            "A cryptic ground bird with large yellow eyes for nocturnal activity, "
            "found in stony savannas and rocky hillside scrub."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Spotted_thick-knee",
        "image": None,
        "provinces": ["asir", "jizan"],
    },
    "palestine-sunbird": {
        "slug": "palestine-sunbird",
        "name": "Palestine Sunbird",
        "scientific_name": "Cinnyris osea",
        "class": "birds",
        "short_description": (
            "A tiny nectar-feeding bird with an iridescent blue-violet throat, "
            "hovering hummingbird-like at flowering shrubs and trees."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Palestine_sunbird",
        "image": None,
        "provinces": ["makkah", "madinah", "tabuk"],
    },
    "yemen-serin": {
        "slug": "yemen-serin",
        "name": "Yemen Serin",
        "scientific_name": "Crithagra menachensis",
        "class": "birds",
        "short_description": (
            "A small yellow-green finch found only in the juniper and acacia "
            "woodlands of the Asir highlands and adjacent Yemen."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Yemen_serin",
        "image": None,
        "provinces": ["asir", "jizan"],
    },
    "western-reef-heron": {
        "slug": "western-reef-heron",
        "name": "Western Reef Heron",
        "scientific_name": "Egretta gularis",
        "class": "birds",
        "short_description": (
            "A heron of rocky shores and coral reefs, occurring in both dark-slate "
            "and all-white colour morphs along Saudi coastlines."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Western_reef_heron",
        "image": None,
        "provinces": ["makkah", "jizan", "eastern-province"],
    },

    # ── REPTILES ─────────────────────────────────────────────

    "arabian-sand-boa": {
        "slug": "arabian-sand-boa",
        "name": "Arabian Sand Boa",
        "scientific_name": "Eryx jayakari",
        "class": "reptiles",
        "short_description": (
            "A small, blunt-headed burrowing snake that hunts lizards and rodents "
            "beneath the sand surface, perfectly camouflaged in the desert."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Jayakar%27s_sand_boa",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail"],
    },
    "desert-cobra": {
        "slug": "desert-cobra",
        "name": "Desert Cobra",
        "scientific_name": "Naja haje",
        "class": "reptiles",
        "short_description": (
            "The Egyptian cobra, one of the most venomous snakes in the region, "
            "capable of spreading a wide hood when threatened."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Egyptian_cobra",
        "image": None,
        "provinces": ["makkah", "madinah", "tabuk"],
    },
    "common-chameleon": {
        "slug": "common-chameleon",
        "name": "Common Chameleon",
        "scientific_name": "Chamaeleo chamaeleon",
        "class": "reptiles",
        "short_description": (
            "Europe and Arabia's only true chameleon, a master of colour change "
            "that stalks insects with independently swivelling eyes."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Common_chameleon",
        "image": None,
        "provinces": ["asir", "jizan", "makkah"],
    },
    "stellagama": {
        "slug": "stellagama",
        "name": "Stellagama",
        "scientific_name": "Stellagama stellio",
        "class": "reptiles",
        "short_description": (
            "A robust, spiny-tailed agama that basks prominently on rocks and "
            "stone walls, a common sight on old buildings and cliff faces."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Roughtail_rock_agama",
        "image": None,
        "provinces": ["makkah", "madinah", "tabuk"],
    },
    "sandfish-skink": {
        "slug": "sandfish-skink",
        "name": "Sandfish Skink",
        "scientific_name": "Scincus scincus",
        "class": "reptiles",
        "short_description": (
            "One of nature's most remarkable adaptations — this skink 'swims' "
            "through loose sand using its streamlined body and fringed toes."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sandfish",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "egyptian-spiny-tailed-lizard": {
        "slug": "egyptian-spiny-tailed-lizard",
        "name": "Egyptian Spiny-tailed Lizard",
        "scientific_name": "Uromastyx aegyptia",
        "class": "reptiles",
        "short_description": (
            "One of the largest agamid lizards, a herbivore that shelters in "
            "deep burrows and uses its ringed, spiny tail for defence."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Egyptian_mastigure",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "hail"],
    },
    "ocellated-skink": {
        "slug": "ocellated-skink",
        "name": "Ocellated Skink",
        "scientific_name": "Chalcides ocellatus",
        "class": "reptiles",
        "short_description": (
            "A small, glossy skink with attractive ocellated patterns, found "
            "under rocks and debris near cultivated areas and coasts."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Ocellated_skink",
        "image": None,
        "provinces": ["makkah", "jizan", "eastern-province"],
    },
    "sinai-agama": {
        "slug": "sinai-agama",
        "name": "Sinai Agama",
        "scientific_name": "Pseudotrapelus sinaitus",
        "class": "reptiles",
        "short_description": (
            "The male turns a striking cobalt-blue when breeding, perching on "
            "rocks to display to females and rivals in rocky desert terrain."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Sinai_agama",
        "image": None,
        "provinces": ["tabuk", "hail", "madinah"],
    },
    "painted-saw-scaled-viper": {
        "slug": "painted-saw-scaled-viper",
        "name": "Painted Saw-scaled Viper",
        "scientific_name": "Echis coloratus",
        "class": "reptiles",
        "short_description": (
            "A highly venomous viper responsible for many snakebite incidents, "
            "it produces a sizzling warning by rubbing saw-edged scales together."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Echis_coloratus",
        "image": None,
        "provinces": ["tabuk", "makkah", "madinah", "hail"],
    },
    "arabian-horned-viper": {
        "slug": "arabian-horned-viper",
        "name": "Arabian Horned Viper",
        "scientific_name": "Cerastes gasperettii",
        "class": "reptiles",
        "short_description": (
            "A venomous desert viper with a horn above each eye, moving "
            "by sidewinding across loose sand and ambushing small prey."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Cerastes_gasperettii",
        "image": None,
        "provinces": ["riyadh", "eastern-province", "tabuk"],
    },
    "marsh-frog": {
        "slug": "marsh-frog",
        "name": "Marsh Frog",
        "scientific_name": "Pelophylax ridibundus",
        "class": "reptiles",
        "short_description": (
            "Europe's largest frog, found in permanent water bodies in parts "
            "of northwestern Arabia, its loud chorus fills wetland nights."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Marsh_frog",
        "image": None,
        "provinces": ["tabuk", "madinah"],
    },

    # ── MARINE ───────────────────────────────────────────────

    "bigfin-reef-squid": {
        "slug": "bigfin-reef-squid",
        "name": "Bigfin Reef Squid",
        "scientific_name": "Sepioteuthis lessoniana",
        "class": "marine",
        "short_description": (
            "A large, intelligent cephalopod capable of rapid colour changes, "
            "common in shallow reefs and seagrass beds of the Red Sea."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Bigfin_reef_squid",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "yellow-longnose-butterflyfish": {
        "slug": "yellow-longnose-butterflyfish",
        "name": "Yellow Longnose Butterflyfish",
        "scientific_name": "Forcipiger flavissimus",
        "class": "marine",
        "short_description": (
            "Bright yellow with an extremely elongated snout used to pick "
            "small invertebrates from coral crevices in the Red Sea."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Longnose_butterflyfish",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "blacktip-grouper": {
        "slug": "blacktip-grouper",
        "name": "Blacktip Grouper",
        "scientific_name": "Epinephelus fasciatus",
        "class": "marine",
        "short_description": (
            "A colourful reef fish with distinctive black-tipped dorsal spines, "
            "a common predator in coral reef ecosystems of the Red Sea."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Blacktip_grouper",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "red-sea-clownfish": {
        "slug": "red-sea-clownfish",
        "name": "Red Sea Clownfish",
        "scientific_name": "Amphiprion bicinctus",
        "class": "marine",
        "short_description": (
            "Endemic to the Red Sea and Gulf of Aden, this vibrant orange-and-white "
            "clownfish lives in symbiosis with sea anemones."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Two-band_anemonefish",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "redmouth-grouper": {
        "slug": "redmouth-grouper",
        "name": "Redmouth Grouper",
        "scientific_name": "Aethaloperca rogaa",
        "class": "marine",
        "short_description": (
            "A dark-bodied grouper with a distinctive red-lined mouth, an ambush "
            "predator that lurks among deep coral reef structures."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Redmouth_grouper",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "yellow-edged-lyretail": {
        "slug": "yellow-edged-lyretail",
        "name": "Yellow-edged Lyretail",
        "scientific_name": "Variola louti",
        "class": "marine",
        "short_description": (
            "A stunning, coral-coloured grouper with yellow-margined lyre-shaped "
            "tail fin, prized by divers in Red Sea reef ecosystems."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Yellow-edged_lyretail",
        "image": None,
        "provinces": ["makkah", "jizan"],
    },
    "small-red-scorpionfish": {
        "slug": "small-red-scorpionfish",
        "name": "Small Red Scorpionfish",
        "scientific_name": "Scorpaena notata",
        "class": "marine",
        "short_description": (
            "A well-camouflaged, venomous fish that rests motionlessly on the "
            "seabed waiting to ambush prey, blending perfectly with rock."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Scorpaena_notata",
        "image": None,
        "provinces": ["makkah", "jizan", "eastern-province"],
    },

    # ── INSECTS ──────────────────────────────────────────────

    "monarch-butterfly": {
        "slug": "monarch-butterfly",
        "name": "Monarch Butterfly",
        "scientific_name": "Danaus plexippus",
        "class": "insects",
        "short_description": (
            "The world's most famous migratory butterfly, found wintering in "
            "coastal areas of Arabia on its intercontinental journeys."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Monarch_butterfly",
        "image": None,
        "provinces": ["jizan", "makkah", "eastern-province"],
    },
    "european-mantis": {
        "slug": "european-mantis",
        "name": "European Mantis",
        "scientific_name": "Mantis religiosa",
        "class": "insects",
        "short_description": (
            "The archetypal praying mantis, a master ambush predator that holds "
            "its forelegs folded as if in prayer while stalking insects."
        ),
        "wikipedia_url": "https://en.wikipedia.org/wiki/Mantis_religiosa",
        "image": None,
        "provinces": ["asir", "makkah", "tabuk"],
    },
}

# ─────────────────────────────────────────────────────────────
#  Animal Classes
# ─────────────────────────────────────────────────────────────

CLASSES = {
    "mammals": {
        "slug": "mammals",
        "name": "Mammals",
        "icon": "🦌",
        "description": (
            "From the iconic Arabian Oryx to elusive leopards and playful dolphins, "
            "Saudi Arabia's mammals span desert, mountain, and ocean."
        ),
        "species": [
            "arabian-oryx", "arabian-gazelle", "nubian-ibex", "arabian-sand-gazelle",
            "arabian-leopard", "caracal", "sand-cat", "arabian-red-fox", "arabian-wolf",
            "desert-hedgehog", "brandts-hedgehog", "spinner-dolphin",
            "common-bottlenose-dolphin", "dugong", "hamadryas-baboon", "arabian-jird",
            "cheesmans-gerbil", "lesser-egyptian-jerboa", "cape-hare", "rock-hyrax",
            "egyptian-fruit-bat", "fat-sand-rat", "common-genet", "white-tailed-mongoose",
        ],
    },
    "birds": {
        "slug": "birds",
        "name": "Birds",
        "icon": "🦅",
        "description": (
            "With over 500 species recorded, Saudi Arabia is a critical corridor "
            "for migrating birds, hosting eagles, falcons, and rare endemics."
        ),
        "species": [
            "greater-flamingo", "lesser-flamingo", "great-egret", "grey-heron",
            "mallard", "ruddy-shelduck", "eurasian-teal", "rock-dove", "laughing-dove",
            "golden-eagle", "black-kite", "black-winged-kite", "white-tailed-eagle",
            "eastern-imperial-eagle", "common-buzzard", "egyptian-nightjar",
            "white-stork", "black-stork", "yellow-legged-gull", "lesser-black-backed-gull",
            "white-wagtail", "eurasian-hoopoe", "long-eared-owl", "short-eared-owl",
            "common-moorhen", "jacobin-cuckoo", "saker-falcon", "steppe-eagle",
            "grey-wagtail", "western-yellow-wagtail", "eurasian-curlew", "lesser-kestrel",
            "spotted-eagle-owl", "african-hoopoe", "white-eared-bulbul", "house-sparrow",
            "barn-owl", "little-owl", "pharaoh-eagle-owl", "desert-owl",
            "white-spectacled-bulbul", "asir-magpie", "sandgrouse", "arabian-babbler",
            "trumpeter-finch", "desert-lark", "desert-finch", "crowned-sandgrouse",
            "arabian-wheatear", "arabian-golden-sparrow", "sinai-rosefinch",
            "helmeted-guineafowl", "tawny-eagle", "pied-kingfisher", "spotted-thick-knee",
            "palestine-sunbird", "yemen-serin", "western-reef-heron",
        ],
    },
    "reptiles": {
        "slug": "reptiles",
        "name": "Reptiles",
        "icon": "🦎",
        "description": (
            "Cobras, sand boas, colour-changing chameleons, and sun-basking "
            "agamas — Arabia's reptiles are masters of desert survival."
        ),
        "species": [
            "arabian-sand-boa", "desert-cobra", "common-chameleon", "stellagama",
            "sandfish-skink", "egyptian-spiny-tailed-lizard", "ocellated-skink",
            "sinai-agama", "painted-saw-scaled-viper", "arabian-horned-viper",
            "marsh-frog",
        ],
    },
    "marine": {
        "slug": "marine",
        "name": "Marine",
        "icon": "🐠",
        "description": (
            "The Red Sea and Arabian Gulf harbour some of the world's most "
            "spectacular coral reefs, home to dazzling and unique sea life."
        ),
        "species": [
            "bigfin-reef-squid", "yellow-longnose-butterflyfish", "blacktip-grouper",
            "red-sea-clownfish", "redmouth-grouper", "yellow-edged-lyretail",
            "small-red-scorpionfish",
        ],
    },
    "insects": {
        "slug": "insects",
        "name": "Insects",
        "icon": "🦋",
        "description": (
            "Though small in number here, Saudi Arabia's featured insects include "
            "globally famous migrants and expert predators."
        ),
        "species": [
            "monarch-butterfly",
            "european-mantis",
        ],
    },
}

CLASSES_LIST = list(CLASSES.values())

# ─────────────────────────────────────────────────────────────
#  Featured Species — Extra Data (10 species only)
#  long_description, images, audio, conservation_status,
#  habitat, fun_facts to be filled in later.
# ─────────────────────────────────────────────────────────────

FEATURED_EXTRA = {
    "arabian-oryx": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Vulnerable",
        "habitat": "Desert plains, gravel plains, and sand dunes",
        "fun_facts": [],
    },
    "arabian-leopard": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Critically Endangered",
        "habitat": "Rocky mountains and steep wadis",
        "fun_facts": [],
    },
    "sand-cat": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Sandy and stony desert",
        "fun_facts": [],
    },
    "nubian-ibex": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Vulnerable",
        "habitat": "Steep cliffs and rocky escarpments",
        "fun_facts": [],
    },
    "golden-eagle": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Mountains, cliffs, and open country",
        "fun_facts": [],
    },
    "saker-falcon": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Endangered",
        "habitat": "Open steppes, semi-desert, and cliffs",
        "fun_facts": [],
    },
    "spinner-dolphin": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Coastal and open ocean waters of the Red Sea and Arabian Gulf",
        "fun_facts": [],
    },
    "caracal": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Dry woodland, savanna, scrub, and semi-arid areas",
        "fun_facts": [],
    },
    "hamadryas-baboon": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Rocky hillsides, cliffs, and semi-desert scrub",
        "fun_facts": [],
    },
    "arabian-sand-boa": {
        "long_description": "",
        "images": [],
        "audio": [],
        "conservation_status": "Least Concern",
        "habitat": "Sandy deserts and loose soil substrates",
        "fun_facts": [],
    },
}

FEATURED_SLUGS = set(FEATURED_EXTRA.keys())