"""recipe_box_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from recipe_box_v1.views import index, recipe, author, add_recipe, add_author, login_view, signup_view, logout_view

from recipe_box_v1.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('recipe/', recipe),
    path('author/', views.author, name='author'),
    path('addauthor/', add_author),
    path('addrecipe/', add_recipe, name='userinput'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
