from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        # the __all__ will bring all the field int UserCreationForm
        fields='__all__'


        