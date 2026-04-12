from . import views
from django.urls import path

app_name="main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("Riyadh/", views.riyadh_view, name="riyadh_view"),
    path("Tabuk/", views.tabuk_view, name="tabuk_view"),
    path("Medina/", views.medina_view, name="medina_view"),
    path("Mecca/", views.mecca_view, name="mecca_view"),   
    path("Khobar/", views.khobar_view, name="khobar_view"),
    path("Jeddah/", views.jeddah_view, name="jeddah_view"),
    path("Jazan/", views.jazan_view, name="jazan_view"),
    path("Abha/", views.abha_view, name="abha_view"),
    path("Aljouf/", views.aljouf_view, name="aljouf_view"),
    path("Alula/", views.alula_view, name="alula_view"),
    path("Altaif/", views.taif_view, name="taif_view"),
    path("Alqassim/", views.alqassim_view, name="alqassim_view"),
    path("view/all", views.discover_view, name="discover_view"),
    path("login/", views.login_view, name="login_view"),

]