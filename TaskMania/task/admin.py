from django.contrib import admin
from .models import TaskModel
# Register your models here.

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_title', 'task_desc', 'is_completed', 'assign_date']
