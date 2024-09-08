
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class change_data(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
