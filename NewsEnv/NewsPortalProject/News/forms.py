from django import forms

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comment']
        widgets={
            'comment':forms.Textarea(attrs={'class':'form-control',
            'rows':'3','placeholder':'Post a comment...'})
        }