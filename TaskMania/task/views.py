from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('show_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form':form})


def edit_task(request, id):
    pi = TaskModel.objects.get(pk = id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=pi)
    return render(request, 'edit_data.html', {'form':form})


def delete_task(request, id):
    pi = TaskModel.objects.get(pk = id)
    if request.method == "POST":
        pi.delete()
        return redirect('show_tasks')
