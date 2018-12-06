import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.forms import ModelForm, DateInput, TimeInput, TextInput, EmailInput, forms
from home.models import fundraiser


class fundraiserForm(ModelForm):
    class Meta:
        model = fundraiser
        fields = ['category','Title','goal_amount','beneficiary_name','beneficiary_relation','Fundraiser_story','End_date']
        widgets = {
            'category':
            'Title':TextInput(attrs={'type': 'text'}),
            'End_date': DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Sorry, Invalid Date!")
        return date


