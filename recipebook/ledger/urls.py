from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUploadView

urlpatterns = [
    path("recipe/add", RecipeCreateView.as_view(), name="add"),
    path("recipes/list", RecipeListView.as_view(), name="list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe"),
    path("recipe/add_image", RecipeUploadView.as_view(), name="upload"),
    path("recipe/<int:pk>/add_image", RecipeUploadView.as_view(), name="upload"),
]

app_name = "ledger"