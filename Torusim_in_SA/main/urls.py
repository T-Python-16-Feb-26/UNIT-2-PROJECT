from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view' ),
    path('destinations/', views.destinations_view, name='destinations_view'),
    path('destinations/riyadh/', views.riyadh_view, name="riyadh_view"),
    path('destinations/jeddah/', views.jeddah_view, name="jeddah_view")
]