from django.urls import path

from . import views

# HTTP REQUEST <- HTTP RESPONSE

# dominio/recipes/
urlpatterns = [
    path('', views.home), 
    path('recipes/<int:id>/', views.recipe), 
]
