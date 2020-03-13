from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225) 
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
