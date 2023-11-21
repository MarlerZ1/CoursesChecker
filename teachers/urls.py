from django.contrib import admin
from django.urls import path

from students.views import work_list
from teachers.views import groupList, group, work_check

app_name = 'teachers'
urlpatterns = [
    path('', groupList, name="groupList"),
    path('group/<int:group_id>', group, name="group"),
    path('work/<int:work_id>', work_check, name="workCheck"),
]