from django import forms
from . import models

class ProfileFr(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields="__all__"