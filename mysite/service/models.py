from django.db import models;
from django.db import connection

class register(models.Model):
    First_Name = models.CharField(max_length=50)
    last_Name  = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    Email_ID = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class products(models.Model):
    
    item_img = models.ImageField(upload_to="img/%Y/%m/%d", blank=True)

class products_names(models.Model):
    item_name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    item_img = models.ImageField(upload_to="img/%Y/%m/%d", blank=True)
    

   

    

# Create your models here.


