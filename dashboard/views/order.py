from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def order(request):
    return render(request,'dashboard/order.html')