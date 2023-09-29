from django.shortcuts import render,redirect
from ..models import Product,Category
from ..forms import ProductForm

# Create your views here.

# product
def productView(request):
    products = Product.objects.all() 
    categories = Category.objects.all() 
    print('categories',categories)
    print('products',products)
    return render(request, 'dashboard/product/index.html', {'products': products,'categories':categories})
def productAddView(request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/product')
            return render(
                  request,
                  'dashboard/product/index.html')
            
def productUpdateView(request,id):
     if request.method == 'POST':
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/product')
     
def productDeleteView(request,id):
    if request.method=='POST':
        products=Product.objects.filter(id=id)
        products.delete()
    return redirect('/product')
    

