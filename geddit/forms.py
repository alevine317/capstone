from django import forms
from .models import *

class PostForm(forms.ModelForm):
    subgeddits = forms.ModelMultipleChoiceField(queryset=SubGeddit.objects.all())

    class Meta:
        model = Post
        fields = ('text_content', 'subgeddits')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)