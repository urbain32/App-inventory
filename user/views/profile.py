from django.shortcuts import render,redirect
from ..forms.UpdateUserForm import UpdateUserForm,ProfileUpdateForm

# Create your views here.

# Category
def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    context={

    }
    return render(request, 'user/profile_update.html',context)