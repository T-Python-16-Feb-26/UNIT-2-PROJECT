def preferences(request):
    return {
        'theme': request.COOKIES.get('theme', 'dark'),
    }
