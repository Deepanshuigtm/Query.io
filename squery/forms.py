# forms.py
from django import forms
from .models import QueryPost

class PostForm(forms.ModelForm):
    class Meta:
        model = QueryPost
        fields = ['title','description', 'image']
