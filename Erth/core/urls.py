from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breeds/', views.breeds, name='breeds'),
    path('impact/', views.impact, name='impact'),
    path('festivals/', views.festivals, name='festivals'),
    path('stories/', views.stories, name='stories'),
    path('science/', views.science, name='science'),
    path('map/', views.map_page, name='map'),
    path('future/', views.future, name='future'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_page, name='login'),
]