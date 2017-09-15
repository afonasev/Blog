from django import forms

from . import models


class CommentForm(forms.ModelForm):

    username = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = models.Comment
        fields = ['username', 'text']
