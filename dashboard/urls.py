from django.urls import path
# for our function in views to be displayed we must import them 
from . import views

# calling our function in views
# path(giving url path name,name of the function in views,name we want to give our function)
urlpatterns=[
    path('',views.index,name='dashboard-index'),
    path('product/',views.index,name='dashboard-product'),
]