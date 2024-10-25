from django import forms

class UsersForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
    