from django.contrib import admin

from teachers.models import Task, Feedback


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']

admin.site.register(Feedback)