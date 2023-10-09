from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Category
def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm()
    context={'form':form}
    return render(request, 'user/register.html',context)