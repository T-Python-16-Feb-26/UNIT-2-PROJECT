
ALLOWED_THEMES = {"light", "dark"}

def theme(request):
    """Inject the current theme into every template context."""
    current = request.COOKIES.get("theme", "light")
    if current not in ALLOWED_THEMES:
        current = "light"
    return {"theme": current}