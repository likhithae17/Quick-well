from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from .models import user_profile, user_appointment

class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class profile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ('name', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)
class appointment(forms.ModelForm):
    class Meta:
        model = user_appointment
        fields = ('name', 'doctor', 'age', 'email', 'contact_number', 'specialisations')
