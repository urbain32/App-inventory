from django.shortcuts import render,redirect
from ..models import Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

# Category
@login_required(login_url='user-login')
def categoryView(request):
    categories = Category.objects.all() 
    return render(request, 'dashboard/category/index.html', {'categories': categories})
def categoryAddView(request):
        if request.method == 'POST':
            name=request.POST.get('name')
            cat=Category(name=name)
            cat.save()
            messages.success(request, 'Category added successfully.') 
            return redirect('/category')
        return render(
                  request,
                  'dashboard/category/index.html')

def edit(request):
    categories=Category.objects.all()
    context={
        "categories":categories
    }
    return redirect(
                  request,
                   'app/pays/index.html',context)

def update(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        cat=Category(
            id=id,
            name=name,
        )
        cat.save()
        messages.success(request, 'Category updated successfully.') 
        return redirect('/category')
    
def delete(request,id):
    if request.method=='POST':
        categories=Category.objects.filter(id=id)
        categories.delete()
        messages.success(request, 'Category delete successfully.') 
    return redirect('/category')