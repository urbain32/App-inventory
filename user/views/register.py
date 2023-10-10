from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from ..forms.RegisterForm import CreateUserForm

# Create your views here.

# Category
def registerView(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-register')
    else:
        form = CreateUserForm()
    context={'form':form}
    return render(request, 'user/register.html',context)