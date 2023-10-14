from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request,'dashboard/home_page/index.html')

