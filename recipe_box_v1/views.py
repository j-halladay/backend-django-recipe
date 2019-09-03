from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from recipe_box_v1.models import Recipe, Author, User
from recipe_box_v1.forms import RecipeForm, AuthorForm, SignupForm, LoginForm, EditForm


def index(request, *args, **kwargs):
    html = 'index.html'
    items = Recipe.objects.all()

    return render(request, html, {'recipe_titles': items})


def recipe(request, *args, **kwargs):
    html = 'recipe.html'
    recipes = Recipe.objects.all()
    return render(request, html, {'recipes': recipes})


def author(request, id, *args, **kwargs):
    html = 'author.html'
    author = Author.objects.get(id=id)
    items = Recipe.objects.all().filter(author=author)
    favorites = author.favorites.all()
    return render(request, html, {'author': author, 'recipes': items, 'favorites': favorites})


@login_required
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
                instructions=data['instructions'], author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeForm()

    return render(request, html, {'form': form})


def add_author(request, *args, **kwargs):
    html = 'addauthor.html'

    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('userinput'))

    form = AuthorForm()

    return render(request, html, {'form': form})


def signup_view(request, *args, **kwargs):
    html = 'signup.html'

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(user=u, name=data['name'])
            login(request, u)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()

    return render(request, html, {'form': form})


def login_view(request, *args, **kwargs):
    html = 'login.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def edit(request, id, *args, **kwargs):
    html = 'edit.html'
    prepop = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prepop.title = data['title']
            prepop.description = data['description']
            prepop.time_required = data['time_required']
            prepop.instructions = data['instructions']
            prepop.save()
            return HttpResponseRedirect(reverse('homepage'))

    form = EditForm(initial={'title': prepop.title, 'description': prepop.description,
                             'time_required': prepop.time_required, 'instructions': prepop.instructions})
    return render(request, html, {'form': form})


@login_required
def favorite(request, id, *args, **kwargs):
    recipe = Recipe.objects.get(id=id)
    u = Author.objects.get(id=request.user.author.id)
    print("author: " + str(u), "recipie: " + str(recipe))
    u.favorites.add(recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfavorite(request, id, *args, **kwargs):
    recipe = Recipe.objects.get(id=id)
    u = Author.objects.get(id=request.user.author.id)
    u.favorites.remove(recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
