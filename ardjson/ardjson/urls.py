from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from . import views

# router = routers.SimpleRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('json/', views.jsonView, name='json'),    
    path('humidity/', views.humidityView, name='humidity'),    
]

