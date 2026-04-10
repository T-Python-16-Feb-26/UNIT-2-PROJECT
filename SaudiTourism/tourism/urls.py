from django.urls import path
from . import views

app_name = 'tourism'
urlpatterns =[
    path('',views.home_view,name='home_view'),
    path('riyadh/',views.riyadh_view,name='riyadh_view'),
    path('makkah/',views.makkah_view,name='makkah_view'),
    path('madinah/',views.madinah_view,name='madinah_view'),
    path('qassim/',views.qassim_view,name='qassim_view'),
    
]