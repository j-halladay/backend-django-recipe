from django import forms
from recipe_box_v1.models import Author

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=300)

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description=forms.CharField(max_length=300)
    time_required=forms.CharField(max_length=4)
    instructions = forms.CharField(max_length=800)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    
# simple form (from basic import), or model form (forms.Form) which links directly to your database model and creates a form for you. It's not readily modifiable, though.