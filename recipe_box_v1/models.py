from django.db import models 

class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    description=models.CharField(max_length=300)
    time_required=models.IntegerField(max_length=4)
    instructions = models.TextField(max_length=800)
    
    def __str__(self):
        return f"{self.title} - {self.author}"
        