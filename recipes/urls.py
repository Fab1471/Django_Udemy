from django.urls import path
from . import views

app_name = 'recipes' # com o app_name não é preciso passar o recipes no name da url no path

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
