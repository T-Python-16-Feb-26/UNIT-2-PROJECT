from django.urls import path
from . import views
app_name = "main"


urlpatterns = [
    path('',views.home_view, name="home_view"),
    path('traditional-clothing/',views.clothing_view, name="clothing_view"),
    path('traditional-foods/',views.foods_view, name="foods_view"),
    path('traditional-games/',views.game_view, name="game_view"),
    path('Handicrafts/', views.handicrafts_view, name="handicrafts_view"),
    path('performing-arts/', views.folk_arts_view, name="folk_arts_view"),
    path('traditions/', views.traditions_view, name="traditions_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),
]
