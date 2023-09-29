from django.urls import path
# for our function in views to be displayed we must import them 
from .views import dashboard,staff,product,order,category

# calling our function in views
# path(giving url path name,name of the function in views,name we want to give our function)
urlpatterns=[
    path('',dashboard.index,name='dashboard-index'),
    path('staff/',staff.staff,name='dashboard-staff'),
    path('order/',order.order,name='dashboard-order'),
    # category
    path('category/',category.categoryView,name='dashboard-category'),
    path('category/add',category.categoryAddView,name='create_category'),
    path('category/update/<int:id>',category.update,name="category_update"),
    path('category/delete/<int:id>',category.delete,name="category_delete"),
    # product
    path('product/',product.productView,name='dashboard-product'),
    path('product/add',product.productAddView,name='create_product'),
    path('product/update/<int:id>',product.productUpdateView,name="product_update"),





]