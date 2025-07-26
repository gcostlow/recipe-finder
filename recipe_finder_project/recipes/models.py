from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField()  # Make sure prep_time exists and is an IntegerField
    servings = models.IntegerField()  # Ensure servings exists as an IntegerField
    
    def __str__(self):
        return self.title