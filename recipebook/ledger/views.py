from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ledger.models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"

class RecipeDetailView(DetailView, LoginRequiredMixin):
    model = Recipe
    template_name = "recipe_detail.html"

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_add.html"

class RecipeUploadView(CreateView):
    model = Recipe
    form_class = RecipeImageForm
    template_name = "recipe_add_image.html"

    def get_success_url(self):
        return reverse_lazy("ledger:recipe", kwargs={"pk": self.object.pk})

    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        form = RecipeImageForm()

        ctx = {"recipe": recipe, "form": form}
        
        return render(request, "recipe_add_image.html", ctx)

    def post(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            image = RecipeImage()
            image.image = form.cleaned_data.get("image")
            image.desc = form.cleaned_data.get("desc")
            image.recipe_image = recipe
            image.save()
            return redirect("ledger:recipe", pk=recipe.pk)
        
        ctx = {"recipe": recipe, "form": form}

        return render(request, "recipe_add.html", ctx)