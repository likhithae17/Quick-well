import datetime
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, DateInput, Select, TextInput, NumberInput, forms
from home.models import fundraiser


class fundraiserForm(ModelForm):
    class Meta:
        category = [
            ('medical','Medical'),
            ('ngo','NGO'),
            ('hospital','Hospital'),
            ('clinic','Clinic'),
        ]

        model = fundraiser
        fields = ['category','Title','goal_amount','beneficiary_name','beneficiary_relation','Fundraiser_story','End_date']
        widgets = {
            'category':Select(choices=category),
            'Title':TextInput(attrs={'type': 'text'}),
            'goal_amount':NumberInput(attrs={'type': 'float'}),
            'beneficiary_name': TextInput(attrs={'type': 'text'}),
            'beneficiary_relation': TextInput(attrs={'type': 'text'}),
            'Fundraiser_story': TextInput(attrs={'type': 'text'}),
            'End_date': DateInput(attrs={'type': 'date'}),
        }

        helper = FormHelper()
        helper.form_method = 'POST'

    def clean_date(self):
        date = self.cleaned_data['End_date']
        if date < datetime.date.today():
            raise forms.ValidationError("Sorry, Invalid Date!")
        return date


