from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm 
from django.shortcuts import get_object_or_404
# Create your models here.


def add_task(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            task = Task.objects.create(title=title, user=request.user)
            return redirect('index')
    return render(request, 'index.html', {'form': form, 'tasks': Task.objects.filter(user=request.user)})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')

def finish_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.status =  1
        task.save()
        return redirect('index')