from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']


class ActivateForm(forms.Form):
    code=forms.CharField(max_length=75)

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        # fields='__all__'
        exclude=('user','code','join_at')