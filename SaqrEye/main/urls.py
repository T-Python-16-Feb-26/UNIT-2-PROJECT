from django.urls import path
from . import views

app_name="main"

urlpatterns=[

    path('',views.persona_view, name="persona_view"),
    path('home/',views.home_view,name="home_view"),
    
]