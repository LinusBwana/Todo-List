from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    completed_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'user', 'completed_status')  # <-- Key line
    search_fields = ('title', 'description')  # Optional: search bar
    list_filter = ('due_date', 'user')  # Optional: filters on the sidebar
    