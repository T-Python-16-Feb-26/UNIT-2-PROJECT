from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("land/forces/", views.land_forces_view, name="land_forces_view"),
    path("air/forces/", views.air_forces_view, name="air_forces_view"),
    path("naval/forces/", views.naval_forces_view, name="naval_forces_view"),
    path("air/defense/forces/", views.air_defense_forces_view, name="air_defense_forces_view"),
    path("strategic/missile/force/", views.strategic_missile_force_view, name="strategic_missile_force_view"),
    path("military/system/", views.military_system_view, name="military_system_view"),
    path("heroes/", views.heroes_view, name="heroes_view"),
    path("technology/", views.technology_view, name="technology_view"),
    path("mode/<mode>/", views.mode_view,name="mode_view"),
]