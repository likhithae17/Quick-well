from django import forms

from .models import user_profile, user_appointment

class profile(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ('name', 'age', 'dob', 'email', 'contact_number', 'address', 'city', 'district', 'state', 'country', 'zipcode', 'photo',)
class appointment(forms.ModelForm):
    class Meta:
        model = user_appointment
        fields = ('name', 'doctor', 'age', 'email', 'contact_number', 'specialisations')
