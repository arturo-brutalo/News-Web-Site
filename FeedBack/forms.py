from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(required=True, min_length=1, max_length=50)
    email_adress = forms.EmailField(required=True)