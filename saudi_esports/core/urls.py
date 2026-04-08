from django.urls import path
from . import views

app_name ="core"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('base/', views.base_view,name='base_view'),
    path('about/', views.about_view,name='about_view'),
    path('game/', views.game_view,name='game_view'),
    path('teams/', views.teams_view,name='teams_view'),
    path('infrastructure/', views.infrastructure_view,name='infrastructure_view'),
    path('events/', views.events_view,name='events_view'),
    path('timeline/', views.timeline_view,name='timeline_view'),

]
