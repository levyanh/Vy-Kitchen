from django.shortcuts import render, redirect
from .models import Profile, Recipe, Comment


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def about (request):
    return render(request, 'about.html')

def profile (request):
    return render(request, 'profile.html')

# def recipe_detail(request, recipe_id):
#     recipe = Recipe.objects.get(id=recipe_id)
#     return render(request, 'recipe_detail.html', {'recipe': recipe})
