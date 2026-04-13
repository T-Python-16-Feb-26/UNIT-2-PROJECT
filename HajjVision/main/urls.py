
from django.urls import path
from . import views
app_name = "main"

urlpatterns = [

    path("set-theme/", views.set_theme, name="set_theme"),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goals/', views.goals, name='goals'),
    path('focus/', views.focus, name='focus'),
    path('targets/', views.targets, name='targets'),
    path('baseline/', views.baseline, name='baseline'),
    path('strategy/', views.strategy, name='strategy'),    
]
