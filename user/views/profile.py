from django.shortcuts import render,redirect
from ..forms.UpdateUserForm import UpdateUserForm,ProfileUpdateForm

# Create your views here.

# Category
def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method =='POST':
        # instance helps to show current data of user
        # instance helps also to show current data of user if with file
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)       
    context={
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'user/profile_update.html',context)