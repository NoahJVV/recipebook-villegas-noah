from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ("image", "desc", "recipe_image")