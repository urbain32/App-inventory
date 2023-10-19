from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    staff= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    pone=models.CharField(max_length=20,null=True)