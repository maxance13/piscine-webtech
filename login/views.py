from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('..') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'login/signup.html', {'form': form})
  
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('..') 
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('..') 