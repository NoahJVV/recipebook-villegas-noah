from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Recipe, RecipeIngredient, RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredient, RecipeImage]
    fieldsets = [
        (
            "Details",
            {
                "fields": [
                    ("name", "author"),
                ]
            },
        )
    ]

class RecipeIngredient(admin.TabularInline):
    model = RecipeIngredient

class RecipeImage(admin.StackedInline):
    model = RecipeImage

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)