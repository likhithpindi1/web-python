from django.db import models;

class service(models.Model):
    First_Name = models.CharField(max_length=100)
    last_Name =models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    Email_ID = models.EmailField()
    password = models.CharField(max_length=100)
    re_enter_password = models.CharField(max_length=100)


    

# Create your models here.

