from django.db import models
from datetime import date
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=150)
    task_desc= models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(default=date.today)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.task_title