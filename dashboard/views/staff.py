from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def staff(request):
    return render(request,'dashboard/staff.html')

