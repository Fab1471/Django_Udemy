from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fabri',
    })

def sobre(request):
    return HttpResponse("Sobre, Django!")


def contato(request):
    return render(request, 'me-apague/temp.html')
