from django.contrib import admin
from django.urls import path

from users.views import login, logout

app_name = "urls_app"

urlpatterns = [
    path('', login, name="login"),
    path('', logout, name="logout")
]
