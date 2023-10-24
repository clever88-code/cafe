from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView


class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForms(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
