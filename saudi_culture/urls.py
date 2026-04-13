from django.urls import path
from . import views

app_name = 'saudi_culture'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('culture/<slug:slug>/', views.culture_view, name='culture_page'),
    path('culture/<slug:slug>/<slug:section>/', views.section_detail_view, name='section_detail'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('chatbot-api/', views.chatbot_response, name='chatbot_api'),
]
