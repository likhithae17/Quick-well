from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from home.models import user_profile
from home.models import user_reports

class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class profile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ( 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo')

class upload(forms.ModelForm):
    class Meta:
        model = user_reports
        fields = ('username', 'file')

class profile_update(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ( 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo')
