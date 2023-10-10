from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()
    firstname=forms.CharField()

    class Meta:
        model=User
        # the __all__ will bring all the field int UserCreationForm
        fields=['firstname','username','email','password1','password2']


        