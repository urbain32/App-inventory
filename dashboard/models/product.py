from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=25,null=False,unique=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT) 
    quantity = models.PositiveIntegerField(null=True)
    class Meta:
        verbose_name_plural = 'Product' # tin our admin the name will be Product not productsa
    def __str__(self):
        return f'{self.name}-{self.quantity}'