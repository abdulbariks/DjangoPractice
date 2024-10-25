from django import forms
from django.forms.widgets import NumberInput, SelectDateWidget 
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985']  
Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]  

class UsersForm(forms.Form):
    name = forms.CharField(max_length=200)
    # email = forms.EmailField()  
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3})) 
    agree = forms.BooleanField()   
    # date_of_birth = forms.DateField()  
    # date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'}))  
    date_of_birth = forms.DateField(widget = SelectDateWidget(years=BIRTH_YEAR_CHOICES))  
    value = forms.DecimalField()  
    # rank = forms.ChoiceField(choices=Choice_value)  
    rank = forms.ChoiceField(widget = forms.RadioSelect, choices=Choice_value)  
    message = forms.CharField(max_length=100, label="Please write a message for us")  