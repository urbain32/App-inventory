from django.shortcuts import render,redirect
from ..models import Product,Category
from ..forms import ProductForm

# Create your views here.

# product
def productView(request):
    products = Product.objects.all() 
    categories = Category.objects.all() 
    return render(request, 'dashboard/product/index.html', {'products': products,'categories':categories})
def productAddView(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/product')

