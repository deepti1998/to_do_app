# Generated by Django 2.1.2 on 2019-03-06 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_due_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_time',
            field=models.TimeField(default=datetime.time(19, 38, 10, 183965)),
        ),
    ]