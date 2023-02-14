from django.contrib import admin
from service.models import service

class serviceAdmin(admin.ModelAdmin):
    register = ('First_Name','last_Name''phone_number', 'Email_ID','password','re_enter_passwor')

admin.site.register(service,serviceAdmin)

# Register your models here.

