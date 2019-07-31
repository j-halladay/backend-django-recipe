from django.shortcuts import render

from recipe_box_v1.models import Recipe


def index(request, *args, **kwargs):
    html = 'index.html'
    items = Recipe.objects.all()
    
    return render(request, html, {'recipes': items}, 'index.html')