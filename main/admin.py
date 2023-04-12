from django.contrib import admin
from .models import Todo, TodoItems

# Register your models here.
admin.site.register(Todo)
admin.site.register(TodoItems)