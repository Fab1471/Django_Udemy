from django.shortcuts import get_list_or_404, get_object_or_404, render
#from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'pages/home.html', context={
        'recipes': recipes, # [make_recipe() for _ in range(10)], # list_comprehension
    })

def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True,
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404('Not Found 🥲')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
     ).order_by('-id')
)

    return render(request, 'pages/category.html', context={
        'recipes': recipes, # [make_recipe() for _ in range(10)], # list_comprehension
        'title': f'{recipes[0].category.name} - Category | '
    })

def recipe(request, id):
    # recipe = Recipe.objects.filter(
    #     pk=id,
    #     is_published=True,
    # ).order_by('-id').first()
    
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    
    return render(request, 'pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
