from django.contrib import admin
from .models import Country, Category, Recipe, Ingredient, Step, Allergen, RecipeIngredient, IngredientAllergen

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(Allergen)
admin.site.register(RecipeIngredient)
admin.site.register(IngredientAllergen)
