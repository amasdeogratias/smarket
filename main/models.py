from email.headerregistry import Group
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    Code = models.CharField(max_length=200, null=True)
    Unit = models.CharField(max_length=200, null=True)
    # category = models.OneToOneField(Category,on_delete=models.CASCADE)
    
    
    def __str__(self): 
        return self.Name

class Catalog(models.Model):
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True)
    user =models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product
        
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True)
    sub_category = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
        
       
    
    

        
    
