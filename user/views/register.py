from django.shortcuts import render

# Create your views here.

# Category
def registerView(request):
    return render(request, 'user/register.html')