from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, JsonResponse
from .models import CultureFact
from google import genai
import os
from dotenv import load_dotenv


def home_view(request):
    return render(request, 'saudi_culture/home.html')


CULTURE_TEMPLATES = {
    'material-culture': 'saudi_culture/material_culture.html',
    'social-life':      'saudi_culture/social_life.html',
    'symbols-language': 'saudi_culture/symbols_language.html',
    'traditions':       'saudi_culture/traditions.html',
    'cuisine':          'saudi_culture/cuisine.html',
    'heritage-gallery': 'saudi_culture/heritage_gallery.html',
    'music':            'saudi_culture/music.html',
}


def culture_view(request, slug):
    template = CULTURE_TEMPLATES.get(slug)
    if template is None:
        raise Http404("Page not found")
    return render(request, template)


SECTION_TEMPLATES = {
    ('material-culture', 'architecture'): 'saudi_culture/sections/material_architecture.html',

    ('social-life', 'majlis'): 'saudi_culture/sections/social_majlis.html',

    ('cuisine', 'main-dishes'):   'saudi_culture/sections/cuisine_main_dishes.html',
    ('cuisine', 'coffee-ritual'): 'saudi_culture/sections/cuisine_coffee.html',
    ('cuisine', 'sweets'):        'saudi_culture/sections/cuisine_sweets.html',

    ('heritage-gallery', 'sadu'):        'saudi_culture/sections/heritage_sadu.html',
    ('heritage-gallery', 'calligraphy'): 'saudi_culture/sections/heritage_calligraphy.html',
    ('heritage-gallery', 'pottery'):     'saudi_culture/sections/heritage_pottery.html',
    ('heritage-gallery', 'jewelry'):     'saudi_culture/sections/heritage_jewelry.html',
}


def section_detail_view(request, slug, section):
    template = SECTION_TEMPLATES.get((slug, section))
    if template is None:
        raise Http404("Section not found")
    return render(request, template)


def toggle_theme(request):
    referer = request.META.get('HTTP_REFERER', '/')
    response = HttpResponseRedirect(referer)
    current = request.COOKIES.get('theme', 'light')
    new_theme = 'dark' if current == 'light' else 'light'
    response.set_cookie('theme', new_theme, max_age=365 * 24 * 60 * 60, samesite='Lax')
    return response

load_dotenv()
def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        
        facts = CultureFact.objects.all()
        context_data = " ".join([f.content for f in facts])

        my_secret_key = os.getenv("GEMINI_API_KEY")
        
        client = genai.Client(api_key=my_secret_key)
        
        prompt = f"""
        You are a Saudi Culture expert. Use this data: {context_data}.
        
        User Question: {user_message}
        
        STRICT RULES FOR YOUR ANSWER:
        1. Be extremely concise. Keep your answer under 3 sentences.
        2. Speak in a friendly, conversational tone.
        3. DO NOT use any Markdown formatting (no asterisks **, no hashes ###, no bullet points). Use only plain text.
        """
        
        # 4. Ask the model
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Using the newer model supported by the new SDK
            contents=prompt
        )
        
        return JsonResponse({'reply': response.text})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)