from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.jsonView, name='json'),    
    path('humidity/', views.humidityView, name='humidity'),    
]

