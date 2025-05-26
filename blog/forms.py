from django import forms
from .models import Post,Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['user','review','rate']
