from django.urls import path
from . import views

app_name="main"

urlpatterns=[

    path('',views.persona_view, name="persona_view"),
    path('set/<str:user_type>/',views.set_persona, name='set_persona')
    path('home/',views.home_view,name="home_view"),
    
]