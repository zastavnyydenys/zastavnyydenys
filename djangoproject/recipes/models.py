from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.country_name


class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    preparation_time = models.PositiveIntegerField()
    nation = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title


class Step(models.Model):
    step_number = models.PositiveIntegerField()
    instruction = models.CharField(max_length=40)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')

    def __str__(self):
        return f"Step {self.step_number} of {self.recipe.title}"


class Ingredient(models.Model):
    name = models.CharField(max_length=40, unique=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient_recipes')

    class Meta:
        unique_together = ('recipe', 'ingredient')


class Allergen(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class IngredientAllergen(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='allergens')
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE, related_name='ingredients')

    class Meta:
        unique_together = ('ingredient', 'allergen')
