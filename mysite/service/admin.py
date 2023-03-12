from django.contrib import admin
from django.contrib.admin.sites import site
from service.models import register
from service.models import products
from service.models import products_names


class serviceAdmin(admin.ModelAdmin):
    register = ('First_Name','last_Name''phone_number', 'Email_ID','password')

admin.site.register(register,serviceAdmin)
# Register your models here.

class productsAdmin(admin.ModelAdmin):
    products = ('item_img')

admin.site.register(products,productsAdmin)

class products_nameAmin(admin.ModelAdmin):
    products_name = ('item_name','price','item_img')

admin.site.register(products_names,products_nameAmin)
