from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/<int:recipe_id>/', views.recipes_detail, name='detail'),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
]