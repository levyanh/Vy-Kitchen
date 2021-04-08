from django.shortcuts import render, redirect
from .models import Profile, Recipe, Comment
# Create your views here.

def home(request):
    recipe = Recipe.objects.all()
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def profile (request):
    return render(request, 'profile.html')