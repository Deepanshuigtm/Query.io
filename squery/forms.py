# forms.py
from django import forms
from .models import QueryPost,Certificate

class PostForm(forms.ModelForm):
    class Meta:
        model = QueryPost
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['image'].widget = forms.FileInput(attrs={'multiple': True})

class RewardsForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title','description', 'file']
