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
        fields = ( 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)

class upload(forms.ModelForm):
    class Meta:
        model = user_reports
        fields = ('username', 'file')

# class writereview(forms.ModelForm):
#     content = forms.CharField(label = "",widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Write about product','rows':'4','cols':'50'}))
#     rating=forms.IntegerField()
#     class Meta:
#         model = item_review
#         fields = ['content','rating']

# class loginform(forms.Form):
#     #choices=[('Doctor','doctor'),('Patient','patient')]
#     #You = forms.ChoiceField(choices=choices)
#     username = forms.CharField(label="User Name", max_length=150)
#     password = forms.CharField(label="Password", max_length=150)