from django.urls import path
from . import views

urlpatterns = [
    # ─── Persona ──────────────────────────────────────────────────────────────
    path('', views.persona_view, name='persona_view'),
    path('change-persona/', views.change_persona_view, name='change_persona_view'),

    # ─── Language ─────────────────────────────────────────────────────────────
    path('set-language/', views.set_language_view, name='set_language_view'),

    # ─── Main Pages ───────────────────────────────────────────────────────────
    path('home/', views.home_view, name='home_view'),
    path('about/', views.about_view, name='about_view'),

    # ─── Cities & Items ───────────────────────────────────────────────────────
    path('city/<str:city_slug>/', views.city_detail_view, name='city_detail_view'),
    path('city/<str:city_slug>/<str:item_type>/<int:item_id>/', views.item_detail_view, name='item_detail_view'),
]