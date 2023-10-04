from django.db import models
from .product import  Product
from django.contrib.auth.models import User

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True) 
    staff = models.ForeignKey(User,models.CASCADE,null=True) 
    order_quantity=models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Order'
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username} quantity ordered is {self.order_quantity}'


    
