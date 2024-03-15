from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError 
from .forms import RegisterForm, LoginForm
from tasks.models import Task
from tasks.forms import TaskForm 

# Create your views here.

def index(request):
   tasks = Task.objects.filter(user=request.user)
   form = TaskForm()
   return render(request, 'index.html', {'tasks': tasks,'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('login')
        except ValidationError as e: 
            form.add_error(None, e)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
