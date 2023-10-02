from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=25,unique=True,null=False)
    class Meta:
        verbose_name_plural = 'Category'
    def __str__(self) :
        return self.name