from recipes.models import Recipe


class RecipeRepository:
    @staticmethod
    def get_all_recipes():
        return Recipe.objects.all()

    @staticmethod
    def get_recipe_by_id(recipe_id):
        return Recipe.objects.filter(id=recipe_id).first()

    @staticmethod
    def create_recipe(data):
        return Recipe.objects.create(**data)

    @staticmethod
    def update_recipe(recipe_id, data):
        recipe = RecipeRepository.get_recipe_by_id(recipe_id)
        if recipe:
            for key, value in data.items():
                setattr(recipe, key, value)
            recipe.save()
            return recipe
        return None

    @staticmethod
    def delete_recipe(recipe_id):
        recipe = RecipeRepository.get_recipe_by_id(recipe_id)
        if recipe:
            recipe.delete()
            return True
        return False
