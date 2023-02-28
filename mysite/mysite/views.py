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
from django.contrib.auth import authenticate,login



def send_email(to, subject, html_content):
        message = Mail(
                from_email='likhithpindi8@gmail.com', 
                to_emails=to, #'likhithpindi@gmail.com',
                subject= subject, #'Sending with Twilio SendGrid is Fun', 
                html_content= html_content #'<strong>and easy to do anywhere, even with Python</strong>'
                )
        try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                return True
        except :
                pass
                return False






class commonData:
        info = register.objects.all()
        print(info)

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
                'footer_2':'Contact',
                'info':info
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
                                        send_email(Email_ID, "thank you", "link")
                                        return render(request,'login.html',r.data)
                        except:
                                return render(request,'login.html',r.data)
               return render(request,'login.html',r.data)
        def user(request):
                r= commonData()
                print("p")

                if request.method == "POST":
                        print("c")
                        login_email = request.POST.get('login_email')
                        login_password = request.POST.get('login_password')
                        register_email = request.POST.get('email')
                        register_password = request.POST.get('password')
                        user= register.objects.values_list('Email_ID',flat=True)
                        user1 = register.objects.values_list('password',flat=True)

                        print(user)
                        #user1 = authenticate(request,Email_ID=login_email, password= login_password )
                        l = len(user)
                        l1 = len(user1)
                        for i in range(l):
                                for j in range(i+1):
                                        if user[i] == login_email and user1[i] == login_password:
                                                return render(request,'user.html',r.data)
                                        break
                        messages.error(request,"EMAIL ID OR PASSWORD IS INCORRECT")
                        return redirect('login')

                        
                
                       
               
        @api_view()
        def api(request):
                return Response({'status' : 200 , 'message':'this is my first api framework'})
        

        
                
               
               



