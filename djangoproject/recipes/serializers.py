from rest_framework import serializers
from .models import Recipe, Category, Country

class RecipeSerializer(serializers.ModelSerializer):
    nation_name = serializers.CharField(write_only=True)
    category_name = serializers.CharField(write_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'preparation_time', 'description', 'nation_name', 'category_name']

    def create(self, validated_data):
        nation_name = validated_data.pop('nation_name')
        category_name = validated_data.pop('category_name')

        # Перевірка, чи існують ці значення в базі даних
        nation = Country.objects.get(country_name=nation_name)
        category = Category.objects.get(category_name=category_name)

        # Створення нового рецепту з даними
        recipe = Recipe.objects.create(nation=nation, category=category, **validated_data)
        return recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'categoryname']
