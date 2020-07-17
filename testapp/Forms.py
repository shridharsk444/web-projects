from django import forms
from testapp.models import loginmodel

class loginpage(forms.Form):
    username=forms.EmailField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput())

