# forms.py
from django import forms
from .models import QueryPost,Certificate

class PostForm(forms.ModelForm):
    class Meta:
        model = QueryPost
        fields = ['title','description', 'image']

class RewardsForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title','description', 'file']
