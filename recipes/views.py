from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'pages/home.html', context={
        'name': 'Fabri',
    })

def recipe(request):
    return render(request, 'pages/home.html', context={
        'name': 'Fabri',
    })
