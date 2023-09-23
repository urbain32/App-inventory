from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CategoryForm
from .models import Category
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')
def staff(request):
    return render(request,'dashboard/staff.html')
def product(request):
    return render(request,'dashboard/product/index.html')
def order(request):
    return render(request,'dashboard/order.html')
# Category
def categoryView(request):
    categories = Category.objects.all()  # Fetch categories from the database
    print("hhhhhhhhhhhhhhhhhhhhh",categories)
    return render(request, 'dashboard/category/index.html', {'categories': categories})
def categoryAddView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            print("data saved", form)
            # After successfully saving the data, render the same page with the form
            return render(request, 'dashboard/category/index.html', {'form': CategoryForm()})
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category/index.html', {'form': form})
