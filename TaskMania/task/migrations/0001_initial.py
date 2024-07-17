# Generated by Django 5.0.4 on 2024-07-16 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=150)),
                ('task_desc', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assign_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]