from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from service.models import service


class commonData:
      data ={
        'title'   : 'Home Page',
        'name'    :'Strandfield',
        'type_1'  :'Shop',
        'type_2'  :'Restaurant',
        'about'   :'About Us',
        'registration':'Register',
        'login'          :'Login',
        'home':'Home',
        'footer_1': '2023 Strandfield',
        'footer_2':'Contact'
        }
class homepage(commonData):
        def home(request):
            r = commonData()
            return render(request,"Index.html",r.data)
        def shop(request):
                r = commonData()
                return render(request,"shop.html",r.data)
        def register(request):
                r= commonData()
                
                
                       
                if request.method == "POST":
                                
                                First_Name = request.POST.get("first_name")
                                last_Name = request.POST.get("last_name")
                                phone_number = request.POST.get("phone_number")
                                Email_ID = request.POST.get("email")
                                password = request.POST.get("password")
                                re_enter_password = request.POST.get("re-password")
                                to_send = service(First_Name = First_Name,last_Name = last_Name, phone_number=phone_number, Email_ID =  Email_ID,password=password,re_enter_password=re_enter_password)
                                to_send.save()
                                

                return render(request,'register.html',r.data)
        def login(request):
               r = commonData()
               if request.method == 'POST':
                                First_Name = request.POST.get("first_name")
                                last_Name = request.POST.get("last_name")
                                phone_number = request.POST.get("phone_number")
                                Email_ID = request.POST.get("email")
                                password = request.POST.get("password")
                                to_send = service(First_Name = First_Name,last_Name = last_Name, phone_number=phone_number, Email_ID =  Email_ID,password=password)
                                to_send.save()
               get_data = service.objects.all()


               return render(request,"login.html",{'get_it' :get_data})
               
               


    


