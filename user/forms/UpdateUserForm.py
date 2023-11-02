from django import forms
from ..models import Profile
from django.contrib.auth.models import User

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['firstname','username','email']

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
        model=Profile
        fields=['address','phone','image']