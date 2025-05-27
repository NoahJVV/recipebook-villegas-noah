from django.urls import path
from .views import recipe_1, recipe_2, recipes_list

urlpatterns = {
	path("recipes/list", recipes_list, name="recipes_list"),
	path("recipe/1", recipe_1, name="recipes_1"),
	path("recipe/2", recipe_2, name="recipes_2"),
}

app_name = "ledger"