from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_box_v1.models import Recipe, Author
from recipe_box_v1.forms import RecipeForm, AuthorForm

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


def add_recipe(request, *args, **kwargs):
    html = 'addrecipe.html'
   
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'], 
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],author=data['author']
            )
            return  HttpResponseRedirect(reverse('homepage'))
   
    form = RecipeForm()
    
    return render(request, html, {'form': form})            


def add_author(request, *args, **kwargs):
    html = 'addrecipe.html'
   
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )

            return  HttpResponseRedirect(reverse('userinput'))
   
    form = AuthorForm()
    
    return render(request, html, {'form': form})   