from email.headerregistry import Group
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    sub_categories = models.ManyToManyField("self")
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
        
        
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    code = ShortUUIDField(
        length=5, 
        max_length=40,
        prefix="code_",
        alphabet="abc1234",
        )
    UNITS = (("DZ", "dozen"), ("LT", "litre"), ("PC", "piece"))    
    unit = models.CharField(max_length=2, null=True, choices=UNITS)
    category = models.ManyToManyField(Category)
    image = models.ImageField(null=True, blank=True)
    
    
    
    def __str__(self): 
        return self.name + "|" + self.category
        
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




        
       
    
    

        
    
