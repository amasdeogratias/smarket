from email.headerregistry import Group
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    sub_categories = models.ManyToManyField("self")
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
        
        
class Product(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    Code = ShortUUIDField(
        length=5, 
        max_length=40,
        prefix="code_",
        alphabet="abc1234",
        )
    UNITS = (("DZ", "dozen"), ("LT", "litre"), ("PC", "piece"))    
    Unit = models.CharField(max_length=2, null=True, choices=UNITS)
    category = models.ManyToManyField(Category)
    
    
    
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


        
       
    
    

        
    
