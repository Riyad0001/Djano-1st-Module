from . import models
from django import forms

class add_musician(forms.ModelForm):
    class Meta:
        model=models.Musician
        fields="__all__"