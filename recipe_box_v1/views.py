from django.shortcuts import render

from recipe_box_v1.models import Recipe, Author


def index(request, *args, **kwargs):
    html = 'index.html'
    items = Recipe.objects.all()
    
    return render(request, html, {'recipe_titles': items})

def recipe(request, *args, **kwargs):
    html = 'recipe.html'
    recipes = Recipe.objects.all()
    return render(request, html, {'recipes': recipes})

def author(request, *args, **kwargs):
    html = 'author.html'
    items = Recipe.objects.all()
    
    return render(request, html, {'author': items})