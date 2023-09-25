from django.shortcuts import render,redirect
from ..models import Category

# Create your views here.

# Category
def categoryView(request):
    categories = Category.objects.all() 
    return render(request, 'dashboard/category/index.html', {'categories': categories})
def categoryAddView(request):
        if request.method == 'POST':
            name=request.POST.get('name')
            cat=Category(name=name)
            cat.save()
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
        return redirect('/category')
    
def delete(request,id):
    if request.method=='POST':
        categories=Category.objects.filter(id=id)
        categories.delete()
    return redirect('/category')