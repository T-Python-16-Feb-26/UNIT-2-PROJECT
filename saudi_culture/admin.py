from django.contrib import admin
from .models import CultureFact

@admin.register(CultureFact)
class CultureFactAdmin(admin.ModelAdmin):
    list_display = ('topic',) 