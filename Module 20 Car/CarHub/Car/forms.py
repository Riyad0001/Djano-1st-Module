from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Comment

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
class ComentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields=['name','email','body']

class change_data(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields = ['username','email']