from django.shortcuts import render,redirect
from ..models import Product,Category
from ..forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create product views here.

@login_required
def productView(request):
    products = Product.objects.all() 
    categories = Category.objects.all() 
    return render(request, 'dashboard/product/index.html', {'products': products,'categories':categories})
def productAddView(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')  # Success message
            return redirect('/product')
        else:
            messages.error(request, 'Failed to add the product.')  # Error message
            return redirect('/product')

    return render(request, 'dashboard/product/index.html')
            
def productUpdateView(request,id):
     if request.method == 'POST':
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
        return redirect('/product')
     
def productDeleteView(request,id):
    if request.method=='POST':
        products=Product.objects.filter(id=id)
        products.delete()
        messages.success(request, 'Product deleted successfully.')

    return redirect('/product')
    

