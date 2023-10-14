from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def staff(request):
    return render(request,'dashboard/staff/staff.html')

