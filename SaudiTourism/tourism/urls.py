from django.urls import path
from . import views

app_name = 'tourism'
urlpatterns =[
    path('',views.home_view,name='home_view'),
    path('riyadh/',views.riyadh_view,name='riyadh_view'),
    path('makkah/',views.makkah_view,name='makkah_view'),
    
]