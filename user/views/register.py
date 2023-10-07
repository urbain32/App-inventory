from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Category
def registerView(request):
    return render(request, 'user/register.html')