from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from home.models import *


class Signup_user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class Signup_profile_form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['firstname','lastname','experience', 'doc_photo', 'phone_num', 'specialization']
