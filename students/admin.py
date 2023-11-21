from django.contrib import admin

from students.models import Work


# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['student', 'task']
