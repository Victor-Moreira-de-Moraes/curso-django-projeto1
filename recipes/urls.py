from django.urls import path
from recipes.views import home

# HTTP REQUEST <- HTTP RESPONSE

# dominio/recipes/
urlpatterns = [
    path('', home), # home
]
