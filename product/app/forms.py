from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']


class Identify(forms.Form):
    username=forms.CharField(max_length=100)
class EmailForm(forms.Form):
    to=forms.CharField(max_length=1000) 
    cc=forms.CharField(max_length=1000) 
    sub=forms.CharField(max_length=1000,required=False) 
    body=forms.CharField(max_length=1000,required=False)    