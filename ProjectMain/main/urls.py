from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home_view, name='home'),
    path('class/<slug:class_slug>/', views.class_view, name='class'),
    path('species/<slug:slug>/', views.species_detail_view, name='species_detail'),
    path('set-preference/<str:key>/<str:value>/', views.set_preference, name='set_preference'),
]
