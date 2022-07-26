from email.headerregistry import Group
from django.db import models

# Create your models here.
class Product(models.Model):
    ProductId = models.CharField(max_length=200)
    Name = models.CharField(max_length=200, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    Code = models.CharField(max_length=200, null=True)
    Group = models.CharField(max_length=200, null=True)
    MainGroup = models.CharField(max_length=200, null=True)
    Unit = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self): 
        return self.Name
    

        
    
