from django.db import models
from dashboard.models import category

class Product(models.Model):
    name=models.CharField(max_length=25,null=False,unique=True)
    category = models.ForeignKey(category,on_delete=models.PROTECT) 
    quantity = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.name