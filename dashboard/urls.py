from django.urls import path
# for our function in views to be displayed we must import them 
from . import views

# calling our function in views
# path(giving url path name,name of the function in views,name we want to give our function)
urlpatterns=[
    path('',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('product/',views.product,name='dashboard-product'),
    path('category/',views.category,name='dashboard-category'),
    path('order/',views.order,name='dashboard-order'),
]