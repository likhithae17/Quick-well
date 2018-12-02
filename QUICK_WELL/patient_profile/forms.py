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
<<<<<<< HEAD:QUICK_WELL/patient_profile/forms.py
        fields = ('username', 'name', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)
class appointment(forms.ModelForm):
    class Meta:
        model = user_appointment
        fields = ('name', 'doctor', 'age', 'email', 'contact_number', 'specialisations')
=======
        fields = ('firstname','lastname', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)


# class appointment(forms.ModelForm):
#     class Meta:
#         model = user_appointment
#         fields = ('name', 'doctor', 'age', 'email', 'contact_number', 'specialisations')
>>>>>>> 27d7db1f9ebdd4d77c6e887cc3d573f9f51f549e:QUICK_WELL/force/forms.py
