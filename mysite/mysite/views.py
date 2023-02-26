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
import sendgrid 
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




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
                        user = None
                        try:
                                user = register.objects.values_list('Email_ID',flat=True)
                                if len(user) == 0 :
                                        m = register(First_Name = First_Name,last_Name = last_Name, phone_number = phone_number ,Email_ID = Email_ID, password = password)
                                        m.save()  
                                        transaction.on_commit(r.do_something) 
                                else:
                                        l = len(user)
                                        for i in range(l):
                                                for j in range(i+1):
                                                        if user[i]== Email_ID:
                                                                messages.error(request,"EMAIL ID ALREADY EXIST")
                                                                return redirect('register')
                                                        break
                                        m = register(First_Name = First_Name,last_Name = last_Name, phone_number = phone_number ,Email_ID = Email_ID, password = password)
                                        m.save()  
                                        transaction.on_commit(r.do_something) 
                                        return render(request,'login.html',r.data)
                        except:
                                return render(request,'login.html',r.data)
               return render(request,'login.html',r.data)
        def user(request):
                r= commonData()
                if request.method == "POST":
                        print(0)
                        login_email = request.POST.get('login_email')
                        login_password = request.POST.get('login_password')
                        register_email = request.POST.get('email')
                        register_password = request.POST.get('password')
                        user= register.objects.values_list('Email_ID','password')
                        print(user)
                        for  i,j in user:
                                print(i)
                                print(j)
                                if i == login_email and j == login_password:
                                        print(i)
                                        print(j)
                                        return render(request,'user.html',r.data)
                        else:
                                messages.error(request,"EMAIL ID OR PASSWORD IS INCORRECT")
                                return redirect('login')
                                       
                                  
                return render(request,'user.html',r.data)
        @api_view()
        def api(request):
                return Response({'status' : 200 , 'message':'this is my first api framework'})
        

        def email(request):
                message = Mail(
                from_email='likhithpindi@gmail.com',
                to_emails='likhithpindi@gmail.com',
                subject='Sending with Twilio SendGrid is Fun',
                html_content='<strong>and easy to do anywhere, even with Python</strong>')
                try:
                        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                        response = sg.send(message)
                        print(response.status_code)
                        print(response.body)
                        print(response.headers)
                        return render(request,'user.html',message)
                except :
                        pass
                        return render(request,'user.html',message)
                
               
               



