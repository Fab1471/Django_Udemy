from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'pages/home.html', context={
        'recipes': recipes, # [make_recipe() for _ in range(10)], # list_comprehension
    })

def recipe(request, id):
    return render(request, 'pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
