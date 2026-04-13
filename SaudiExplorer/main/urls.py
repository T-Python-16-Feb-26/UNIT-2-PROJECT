from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('crops/', views.crops_view, name='crops_view'),
    path('regions/', views.regions_view, name='regions_view'),
    path('initiatives/', views.initiatives_view, name='initiatives_view'),
    path('technology/', views.technology_view, name='technology_view'),
    path('records/', views.records_view, name='records_view'),
    path('quiz/', views.quiz_view, name='quiz_view'),
    path('festivals/', views.festivals_view, name='festivals_view'),
    path('dates/', views.dates_view, name='dates_view'),
    
]