from .models import Post,Coment
from django import forms
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        exclude=['author']
class ComentForm(forms.ModelForm):
    
    class Meta:
        model = Coment
        fields=['name','email','body']
