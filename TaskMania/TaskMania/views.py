from django.shortcuts import render
from task.models import TaskModel


def show_tasks(request):
    data = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'data':data})