from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.jsonView, name='json'),    
    path('humidity/', views.humidityView, name='humidity'),
    path('celsius/', views.celsiusView, name='celsius'),    
    path('fahrenheit/', views.fahrenheitView, name='fahrenheit'),
]

