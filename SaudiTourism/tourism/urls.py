from django.urls import path
from . import views

app_name = 'tourism'
urlpatterns =[
    path('',views.home_view,name='home_view'),
    # path('city/<str:city_name>/',views.city_view,name='city_view'),
]