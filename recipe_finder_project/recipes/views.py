from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe

def add_recipe(request):
    # If the form has been submitted (POST request)
    if request.method == 'POST':
        form = RecipeForm(request.POST)  # Create a form instance with the data submitted
        if form.is_valid():  # If the form data is valid
            form.save()  # Save the new recipe to the database
            return render(request, 'recipes/view_recipes.html', {'recipes': Recipe.objects.all()}) # Redirect to the view that displays all recipes
    else:
        form = RecipeForm()  # If it’s a GET request, show an empty form

    return render(request, 'recipes/add_recipe.html', {'form': form})
    # Render the form in a template

def view_recipes(request):
    recipes = Recipe.objects.all()  # Get all recipes from the database
    return render(request, 'recipes/view_recipes.html', {'recipes': recipes})