from django.urls import path
from . import views

urlpatterns = [
    path('recipes/create/', views.recipe_create, name='recipe_create'),
    path('recipes/update/<int:recipe_id>/', views.recipe_update, name='recipe_update'),
    path('recipes/delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'),

    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/report/', views.recipes_report, name='recipes_report'),
]
