from django.shortcuts import render, redirect
from .models import Profile, Recipe, Comment


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def profile (request):
    return render(request, 'profile.html')

def recipe_detail (request):
    recipes = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html')
