import datetime

from crispy_forms.helper import FormHelper
from django.forms import ModelForm, DateInput, TimeInput, TextInput, EmailInput, forms
from home.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','time','user_name','email_id']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'user_name':TextInput(attrs={'type': 'text'}),
            'email_id': EmailInput(attrs={'type':'email'}),
        }

        helper = FormHelper()
        helper.form_method = 'POST'


def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Sorry, Invalid Date!")
        return date



