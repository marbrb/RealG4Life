from django import forms
from core.models import User
from django.contrib.auth import authenticate

class FormLogin(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
