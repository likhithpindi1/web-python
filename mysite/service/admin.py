from django.contrib import admin
from django.contrib.admin.sites import site
from service.models import service

class serviceAdmin(admin.ModelAdmin):
    register = ('First_Name','last_Name''phone_number', 'Email_ID','password')

admin.site.register(service,serviceAdmin)

# Register your models here.
