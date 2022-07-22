from email.headerregistry import Group
from django.db import models

# Create your models here.
class Product(models.Model):
    ProductId = models.CharField(max_length=200)
    Name = models.CharField(max_length=200, null=True)
    Code = models.CharField(max_length=200, null=True)
    Group = models.CharField(max_length=200, null=True)
    MainGroup = models.CharField(max_length=200, null=True)
    Unit = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.Name
        
    
