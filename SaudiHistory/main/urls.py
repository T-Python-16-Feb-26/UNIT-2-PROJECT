from django.urls import path
from . import views

app_name="main"


urlpatterns=[
    path('', views.home_view, name="home_view"),

    path('first-saudi-state/', views.state1_view, name="state1_view"),

    path('second-saudi-state/', views.state2_view, name="state2_view"),

    path('saudi-arabia-kingdom/', views.state3_view, name="state3_view"),
    

    path('king-abdulaziz/', views.king1_view, name="king1_view"),

    path('king-saud/', views.king2_view, name="king2_view"),

    path('king-faisal/', views.king3_view, name="king3_view"),
    
    path('king-khalid/', views.king4_view, name="king4_view"),
    
    path('king-fahd/', views.king5_view, name="king5_view"),
    
    path('king-abdullah/', views.king6_view, name="king6_view"),
    
    path('king-salman/', views.king7_view, name="king7_view"),


    path("mode/light/", views.light_mode_view, name="light_mode_view"),
    path("mode/dark/", views.dark_mode_view, name="dark_mode_view"),

   
   
]