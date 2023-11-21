from django.contrib import admin
from django.urls import path

from students.views import work_list, work_editor, description_async

app_name = 'students'

urlpatterns = [
    path('', work_list, name="workList"),
    path('work/<int:work_id>', work_editor, name="workEditor"),
    path('work/', work_editor, name="workEditor"),
    path('description/get', description_async, name='descriptionAsync')
]
