from django import forms
import re

class QuoteRequestForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'required': 'required'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'required': 'required'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'required': 'required', 'pattern': r'.+@.+\.com$'}))
    phone = forms.CharField(max_length=20, label='Phone Number', widget=forms.TextInput(attrs={'required': 'required', 'pattern': r'^(\+1\s?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}$'}))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'required': 'required'}), label='Job Description')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # US phone number regex: (123) 456-7890, 123-456-7890, 1234567890, +1 123-456-7890
        pattern = re.compile(r'^(\+1\s?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}$')
        if not pattern.match(phone):
            raise forms.ValidationError('Enter a valid US phone number.')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('.com'):
            raise forms.ValidationError('Email must end with .com')
        return email 