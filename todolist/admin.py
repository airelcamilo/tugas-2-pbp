from django.contrib import admin
from .models import Task
from .forms import CreateTask

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    form = CreateTask
admin.site.register(Task, TaskAdmin)