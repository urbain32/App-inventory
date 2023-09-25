from django.shortcuts import render,redirect
from django.http import HttpResponse
from ..forms import CategoryForm
from ..models import Category
from django.views import generic

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

