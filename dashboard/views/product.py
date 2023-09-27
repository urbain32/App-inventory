from django.shortcuts import render,redirect
from ..models import Product,Category

# Create your views here.

# product
def productView(request):
    products = Product.objects.all() 
    categories = Category.objects.all() 
    return render(request, 'dashboard/product/index.html', {'products': products,'categories':categories})

