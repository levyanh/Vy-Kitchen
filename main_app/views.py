from django.shortcuts import render, redirect
from .models import Profile, Recipe, Comment
# Create your views here.

def home(request):
    recipe = Recipe.objects.all()
    return render(request, 'home.html')