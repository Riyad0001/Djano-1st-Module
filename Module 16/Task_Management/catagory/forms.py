from django import forms
from . import models
class CatForm(forms.ModelForm):
    class Meta:
        model=models.CatModel
        fields="__all__"
