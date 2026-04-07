from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('land/', views.land_view, name='land_view'),
    path('people/', views.people_view, name='people_view'),
    path('traditions/', views.traditions_view, name='traditions_view'),
    path('cities/', views.cities_view, name='cities_view'),
    path('royal-family/', views.royal_family_view, name='royal_family_view'),
    path('future/', views.future_view, name='future_view'),
    path('legacy/', views.legacy_view, name='legacy_view'),
    path('celebrations/', views.celebrations_view, name='celebrations_view'),
]