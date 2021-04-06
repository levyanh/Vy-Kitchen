from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.

#Home view
def home(request):
    return render(request, 'home.html')

#About view
def about(request):
    return render(request, 'about.html')

#Recipe_detail view
def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', context)


#Profile view
def profile(request):
    return render(request, 'profile.html')

#Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#Login view
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
                form = login(request, user)
                messages.success(request,' Welcome {username} !!')
                return redirect('profile')
        else:
            messages.info(request,'Please register first')
            form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form,})
    
