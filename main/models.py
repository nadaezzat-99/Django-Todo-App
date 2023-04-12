from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    priority_choices = [
        ('H','High'),
        ('L','Low'),
        ('M','Moderate')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    priority = models.CharField(max_length=1, choices=priority_choices)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description[:50] + '...'


class TodoItems(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
