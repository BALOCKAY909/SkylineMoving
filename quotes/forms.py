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

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Leave blank for Anonymous',
        'id': 'reviewName',
        'aria-required': 'false',
        'data-validate': 'false'
    }))
    rating = forms.ChoiceField(choices=[
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ], required=False, widget=forms.HiddenInput(attrs={'id': 'reviewRating'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Tell us about your experience with Skyline Moving...',
        'id': 'reviewText'
    }), required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get('rating')
        description = cleaned_data.get('description')
        
        # If both rating and description are empty, raise validation error
        if not rating and not description:
            raise forms.ValidationError('Please provide either a rating or a review description.')
        
        # Set defaults for empty fields
        if not cleaned_data.get('name'):
            cleaned_data['name'] = 'Anonymous'
        if not rating:
            cleaned_data['rating'] = 'none'
        if not description:
            cleaned_data['description'] = 'none'
            
        return cleaned_data