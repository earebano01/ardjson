from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
# router.register(r'temperature-data', TemperatureDataViewSet)
# router.register(r'humidity-data')
# router.register(r'fahrenheit-data')
# router.register(r'celsius-data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('json/', views.jsonView, name='json'),    
    path('humidity/', views.humidityView, name='humidity'),
    path('celsius/', views.celsiusView, name='celsius'),    
    path('fahreneheit/', views.fahrenheitView, name='fahrenheit'),    
]

