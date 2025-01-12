# Generated by Django 5.0.4 on 2024-07-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category_name',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='task',
            field=models.ManyToManyField(related_name='categories', to='task.taskmodel'),
        ),
    ]
