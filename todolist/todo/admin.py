from django.contrib import admin
from .models import Task, TaskAdmin

# Register your models here.

admin.site.register(Task, TaskAdmin)
