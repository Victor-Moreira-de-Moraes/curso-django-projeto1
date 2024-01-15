from django.urls import path
from recipes.views import contato, home, sobre

# HTTP REQUEST <- HTTP RESPONSE

# dominio/recipes/
urlpatterns = [
    path('', home), # home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]
