from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=300)
    favorites = models.ManyToManyField("Recipe", related_name="favorites")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    time_required = models.CharField(max_length=4)
    instructions = models.TextField(max_length=800)
    likes = models.ManyToManyField(Author, related_name="likes")

    def __str__(self):
        return f"{self.title} - {self.author}"
