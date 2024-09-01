from . import models
from django import forms

class add_albums(forms.ModelForm):
    class Meta:
        model=models.Album
        fields="__all__"