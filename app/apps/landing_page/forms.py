from email import message
from django import forms


class Contact(forms.Form):
    email = forms.EmailField()
    type = forms.CharField()
    message = forms.CharField()
