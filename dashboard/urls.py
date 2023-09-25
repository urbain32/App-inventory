from django.urls import path
# for our function in views to be displayed we must import them 
from .views import dashboard,staff,product,order,category

# calling our function in views
# path(giving url path name,name of the function in views,name we want to give our function)
urlpatterns=[
    path('',dashboard.index,name='dashboard-index'),
    path('staff/',staff.staff,name='dashboard-staff'),
    path('product/',product.product,name='dashboard-product'),
    path('order/',order.order,name='dashboard-order'),
    path('category/',category.categoryView,name='dashboard-category'),
    path('categoryAdd/',category.categoryAddView,name='create_category'),

]