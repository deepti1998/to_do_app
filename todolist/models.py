from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    content = models.TextField(max_length=2000, blank=True)
    creation_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_time = models.TimeField(default=timezone.now().time())
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


