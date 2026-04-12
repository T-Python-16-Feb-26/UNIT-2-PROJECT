from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view' ),
    path('destinations/', views.destinations_view, name='destinations_view'),
    path('destinations/riyadh/', views.riyadh_view, name="riyadh_view"),
    path('destinations/jeddah/', views.jeddah_view, name="jeddah_view"),
    path('destinations/alula/', views.alula_view, name="alula_view"),
    path('destinations/abha/', views.abha_view, name='abha_view'),
    path('experience/<slug:slug>/', views.experience_detail, name='experience_detail'),
    path('large/font/', views.large_font, name='large_font'),
    path('small/font/', views.small_font, name="small_font"),
    path('search/', views.search_view, name='search_view'),

]