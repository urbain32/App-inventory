from django.db import models
from .product import  Product

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True) 
    
