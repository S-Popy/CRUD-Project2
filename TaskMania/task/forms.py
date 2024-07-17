from django import forms 
from .models import TaskModel 
from category.models import CategoryModel
from django.forms.widgets import NumberInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'assign_date': NumberInput(attrs={'type': 'date'}),
        }
        labels = {'task_desc':'Task Description'}

