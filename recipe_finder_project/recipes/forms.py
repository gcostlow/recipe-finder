from django import forms
from .models import Recipe  # Import the Recipe model so we can create the form based on it

class RecipeForm(forms.ModelForm):  # Create a ModelForm for the Recipe model
    class Meta:
        model = Recipe  # Specify the model this form is associated with
        fields = ['title', 'ingredients', 'instructions', 'prep_time', 'servings']  # The fields we want in the form
