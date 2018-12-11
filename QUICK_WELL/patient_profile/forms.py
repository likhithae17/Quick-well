from attr.filters import exclude
from django import forms
from django.contrib.auth.forms import User, UserCreationForm, UserChangeForm, PasswordChangeForm
from home.models import user_profile, user_reports, User_Review
from home.models import *
from django.forms import ModelForm,Textarea

class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class profile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ( 'username', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo')
# =======
#         fields = ('username', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode',
#                   'photo',)
# >>>>>>> 3c7fb08664ee49ae263b250542b5d5e7d117dd36

class upload(forms.ModelForm):
    class Meta:
        model = user_reports
        fields = ('username', 'file')

class profile_update(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ( 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo')


class Patient_Update_Form(UserChangeForm):
    class Meta:
        model = user_profile
        fields = ('name', 'email', 'contact_number', 'address')

class passwordchange(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = User_Review
        exclude = ('client_accountid',)
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }