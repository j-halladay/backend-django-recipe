from django import forms
from recipe_box_v1.models import Author

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description=forms.CharField(max_length=300)
    time_required=forms.CharField(max_length=4)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class SignupForm(forms.Form):
    name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
# simple form (from basic import), or model form (forms.Form) which links directly to your database model and creates a form for you. It's not readily modifiable, though.