from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def product(request):
    return render(request,'dashboard/product/index.html')
