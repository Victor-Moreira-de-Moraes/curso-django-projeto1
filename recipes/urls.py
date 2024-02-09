from django.urls import path

from . import views

# HTTP REQUEST <- HTTP RESPONSE

app_name = 'recipes'

# dominio/recipes/
urlpatterns = [
    path('', views.home, name="home"), 
    path('recipes/<int:id>/', views.recipe, name="recipe"), 
]
