from django.urls import path
from .views import RecipeListView, RecipeDetailView, index

urlpatterns = {
	path('', index, name = 'ledger'),
	path('recipes/list', RecipeListView.as_view(), name = 'list'),
	path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'recipe')
}

app_name = "ledger"