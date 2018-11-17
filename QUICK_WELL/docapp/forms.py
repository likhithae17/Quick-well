import datetime

from django.forms import ModelForm, DateInput, TimeInput, TextInput, EmailInput, forms
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','time']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'username':TextInput(attrs={'type': 'text'}),
            'emailid': EmailInput(attrs={'type':'email'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Sorry, Invalid Date!")
        return date

