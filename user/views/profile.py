from django.shortcuts import render,redirect

# Create your views here.

# Category
def profile(request):
    return render(request, 'user/profile.html')