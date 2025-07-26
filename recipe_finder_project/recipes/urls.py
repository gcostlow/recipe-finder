from django.urls import path
from . import views  # Import views from the mealplanner app

urlpatterns = [
    path('add_recipe/', views.add_recipe, name='add_recipe'),  # URL for adding recipes
    path('view_recipes/', views.view_recipes, name='view_recipes'),  # URL for viewing recipes
]
