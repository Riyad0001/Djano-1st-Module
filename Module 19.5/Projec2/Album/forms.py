from . import models
from django import forms

class AlbumForm(forms.ModelForm):
    class Meta:
        model=models.Album
        fields="__all__"
        