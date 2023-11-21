from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'loginFormInput',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Введите пароль",
        'class': 'loginFormInput',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']