from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('recipes/', views.home, name='recipes'),
    # path('recipes/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
]
