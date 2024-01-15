from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Moreira',
    })

# HTTP REQUEST
def contato(request):
    return HttpResponse('contato')
    # RETURN HTTP Response

def sobre(request):
    return HttpResponse('sobre')
