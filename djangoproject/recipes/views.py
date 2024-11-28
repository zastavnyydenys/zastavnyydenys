from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Recipe

# List all recipes
# Create a new recipe
def recipe_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        preparationtime = request.POST.get("preparationtime")
        descriptionR = request.POST.get("descriptionR")
        nationid_id = request.POST.get("nationid")
        categorynameid_id = request.POST.get("categorynameid")
        recipe = Recipe.objects.create(
            title=title,
            preparationtime=preparationtime,
            descriptionR=descriptionR,
            nationid_id=nationid_id,
            categorynameid_id=categorynameid_id,
        )
        return JsonResponse({"id": recipe.id, "message": "Recipe created successfully"})

# Update an existing recipe
def recipe_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        recipe.title = request.POST.get("title", recipe.title)
        recipe.preparationtime = request.POST.get("preparationtime", recipe.preparationtime)
        recipe.descriptionR = request.POST.get("descriptionR", recipe.descriptionR)
        recipe.save()
        return JsonResponse({"message": "Recipe updated successfully"})

# Delete a recipe
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return JsonResponse({"message": "Recipe deleted successfully"})

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Recipe
from .serializers import RecipeSerializer
from django.db.models import Count

# 1. Список рецептів
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Деталі рецепту
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        recipe.delete()
        return Response({"message": "Recipe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 3. Агрегований звіт
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recipes_report(request):
    report = (
        Recipe.objects.values("category__category_name")  # Виправлено посилання на поле категорії
        .annotate(total_recipes=Count("id"))
        .order_by("-total_recipes")
    )
    data = [
        {"category": r["category__category_name"], "total_recipes": r["total_recipes"]}
        for r in report
    ]
    return Response(data)
