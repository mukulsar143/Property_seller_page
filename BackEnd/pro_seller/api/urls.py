from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

# routers.register('properties', PropertyViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('properties/', PropertyViewSet.as_view()),
    path('get/', GetProperties, name='get-name'),
]