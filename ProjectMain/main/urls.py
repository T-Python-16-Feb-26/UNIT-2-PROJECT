from django.contrib import admin
from django.urls import path, include
from . import views #import the module views
app_name = "main"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('main'))
    path('',views.home_view,name='home_view'),
]
