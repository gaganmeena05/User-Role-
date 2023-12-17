# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return redirect('signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def logout_view(request):    
    logout(request)
    return redirect('signin')
