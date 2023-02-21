from django.db import models;
from django.db import connection

class register(models.Model):
    First_Name = models.CharField(max_length=50)
    last_Name  = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    Email_ID = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    

   

    

# Create your models here.

