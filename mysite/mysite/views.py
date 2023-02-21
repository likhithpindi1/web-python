from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.db import transaction
from django.forms.models import model_to_dict
from service.models import register
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view 
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
      def do_something(request):
                pass  
class homepage(commonData):
       
        def home(request):
            r = commonData()
            return render(request,"Index.html",r.data)
        def shop(request):
                r = commonData()
                return render(request,"shop.html",r.data)
        def register(request):
                r= commonData()
                return render(request,'register.html',r.data)
        
        def login(request):
               r = commonData()
               if request.method == 'POST':
                        First_Name = request.POST.get("first_name")
                        last_Name = request.POST.get("last_name")
                        phone_number = request.POST.get("phone_number")
                        Email_ID = request.POST.get("email")
                        password = request.POST.get("password")
                        name = register.objects.values_list('Email_ID',flat=True)

                        try:
                                user = register.objects.get(Email_ID = Email_ID)
                        except:
                                messages.error(request,'email id is exist ')
                        user = authenticate(request, Email_ID = Email_ID, password = password )
                        if user is not None:
                                login(request,user)
                                return redirect('home')
                        l =[]
                        print(name[0])
                        for i in name:
                               l.append(i)
                               print(l)
                               for i in l:
                                       if i == Email_ID:
                                               print("email exist")
                                               messages.error(request, 'Email Id Already Exist')
                                       else:
                                               transaction.on_commit(r.do_something)
                                               break   

               return render(request,"login.html",r.data)
        def user(request):
                r= commonData()
                return render(request,'user.html',r.data)
        
        @api_view()
        def api(request):
                return Response({'status' : 200 , 'message':'this is my first api framework'})
               
               



