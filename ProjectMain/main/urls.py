from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home_view, name='home'),
    path('class/<slug:class_slug>/', views.class_view, name='class'),
    path('species/<slug:slug>/', views.species_detail_view, name='species_detail'),
    path('set-preference/<str:key>/<str:value>/', views.set_preference, name='set_preference'),
    path('featured/caracal', views.caracal_view, name='featured_caracal'),
    path('featured/arabian-oryx', views.arabian_oryx_view, name='featured_arabian_oryx'),
    path('featured/sand-cat', views.sand_cat_view, name='featured_sand_cat'),
    path('featured/arabian-leopard', views.arabian_leopard_view, name='featured_arabian_leopard'),
    path('featured/nubian-ibex', views.nubian_ibex_view, name='featured_nubian_ibex'),
    path('featured/golden-eagle', views.golden_eagle_view, name='featured_golden_eagle'),
    path('featured/saker-falcon', views.saker_falcon_view, name='featured_saker_falcon'),
    path('featured/spinner-dolphin', views.spinner_dolphin_view, name='featured_spinner_dolphin'),
    path('featured/hamadryas-baboon', views.hamadryas_baboon_view, name='featured_hamadryas_baboon'),
    path('featured/arabian-sand-boa', views.arabian_sand_boa_view, name='featured_arabian_sand_boa'),
]
