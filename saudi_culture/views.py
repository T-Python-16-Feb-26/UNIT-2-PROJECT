from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, JsonResponse
from .models import CultureFact
from google import genai
import os
from dotenv import load_dotenv


def home_view(request):
    return render(request, 'saudi_culture/home.html')


VALID_CULTURE_SLUGS = {
    'material-culture', 'social-life', 'symbols-language',
    'traditions', 'cuisine', 'heritage-gallery', 'music',
}

VALID_SECTIONS = {
    ('material-culture', 'architecture'),
    ('social-life',      'majlis'),
    ('cuisine',          'main-dishes'),
    ('cuisine',          'coffee-ritual'),
    ('cuisine',          'sweets'),
    ('heritage-gallery', 'sadu'),
    ('heritage-gallery', 'calligraphy'),
    ('heritage-gallery', 'pottery'),
    ('heritage-gallery', 'jewelry'),
}

# Section filename overrides where the section slug doesn't map cleanly to the filename.
SECTION_FILENAME_OVERRIDES = {
    ('cuisine', 'coffee-ritual'): 'coffee',
}


def _culture_template(slug):
    return f'saudi_culture/{slug.replace("-", "_")}.html'


def _section_template(slug, section):
    override = SECTION_FILENAME_OVERRIDES.get((slug, section))
    section_name = override if override else section.replace('-', '_')
    slug_prefix = slug.split('-')[0]
    return f'saudi_culture/sections/{slug_prefix}_{section_name}.html'


def culture_view(request, slug):
    if slug not in VALID_CULTURE_SLUGS:
        raise Http404("Page not found")
    return render(request, _culture_template(slug))


def section_detail_view(request, slug, section):
    if (slug, section) not in VALID_SECTIONS:
        raise Http404("Section not found")
    return render(request, _section_template(slug, section))


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
        
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt
        )
        
        return JsonResponse({'reply': response.text})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)