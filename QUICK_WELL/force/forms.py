from django import forms
from django.contrib.auth.forms import User, UserCreationForm
from home.models import user_profile

class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class profile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ('firstname','lastname', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)


# class appointment(forms.ModelForm):
#     class Meta:
#         model = user_appointment
#         fields = ('name', 'doctor', 'age', 'email', 'contact_number', 'specialisations')
