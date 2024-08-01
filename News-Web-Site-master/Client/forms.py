from django import forms

class CreateContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    surname = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5, max_length=100, widget=forms.TextInput(attrs={"type":'password'}))

class LogInForm(forms.Form):
    name = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5, max_length=100, widget=forms.TextInput(attrs={"type":'password'}))
