from django.db import models
from .product import  Product
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True) 
    staff = models.ForeignKey(User,models.CASCADE,null=True) 
    order_quantity=models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=Truerue)


    
