from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.db import transaction
from django.forms.models import model_to_dict
from service.models import register
from service.models import products
from service.models import products_names
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view 
import sendgrid 
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
from django.contrib.auth import authenticate,login
from mailjet_rest import Client
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def send_email():
        api_key = '' #os.environ['mailjet_api_key']

        api_secret = '' #os.environ['mailjet_api_secret']
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        
        data = {
                'Messages': [
				{
						"From": {
								"Email": "likhithpindi@gmail.com",
								"Name": "Me"
						},
						"To": [
								{
										"Email": "likhithpindi8@gmail.com",
										"Name": "You"
								}
						],
						"Subject": "My first Mailjet Email!",
						"TextPart": "Greetings from Mailjet!",
						"HTMLPart": "<h3>Thank for registration in strandfield  <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
				}
		]
                }
        result = mailjet.send.create(data=data)
        result.status_code    
        result.json()
        





class commonData:

        def do_something(request):
                pass  
class homepage(commonData):
       
        def home(request):
        
            return render(request,"Index.html")
        def shop(request):
                r = commonData()
                
                data ={
                
                'items' :[
                        {"name" : "Basmati Rice 20kg Garimaa Shahi", "price" : '25.00$',  'img':"""/media/img/2023/03/11/large_4f4bfbad4a3f9c4bf9726ff5890a-1-removebg-preview.png"""},
                        {"name" : "White sesame seeds 1 KG", "price" : '27.00$',  'img':"""/media/img/2023/03/11/large_sesame-leves.jpg"""},
                        {"name" : "Toor Daal  2 KG TRS", "price" : '32.00$',  'img':"""/media/img/2023/03/11/large_sam-1109-copy.jpg"""},
                        {"name" : "Tamarind - 400g", "price" : '12.00$',  'img':"""/media/img/2023/03/11/large_IMG-3992.jpg"""},

                        {"name" : "Spicebox 9", "price" : '120.00$',  'img':"""/media/img/2023/03/11/large_s-s-masala-peti-500x500.jpg"""},
                        {"name" : "Ryż Basmati Super JAISAL 5kg", "price" : '15.00$',  'img':"""/media/img/2023/03/11/large_jaisal03.jpg"""},
                        {"name" : "Rice Basmati Exotic/Dubar INDIA GATE 10kg", "price" : '105.00$',  'img':"""/media/img/2023/03/11/large_indiagate-exotic-rice-5kg-little-india.jpg"""},
                        {"name" : "Ryż Basmati Extra Long Premium 10 kg", "price" : '150.00$',  'img':"""/media/img/2023/03/11/large_WhatsApp-Image-2022-11-09-at-6-11-08-PM.jpeg"""},

                        {"name" : "Monaco Jeffs Zeera Biscuits 200G Parle", "price" : '5.00$',  'img':"""/media/img/2023/03/11/large_Parle-Jeff-Jeera-Sixer-Cookies-SDL100973706-2-3795a.jpg"""},
                        {"name" : "Soft Crunch Toast 350G Pran", "price" : '15.00$',  'img':"""/media/img/2023/03/11/large_9-3.jpg"""},
                        {"name" : "Sat Isabgol  100G Pran", "price" : '5.00$',  'img':"""/media/img/2023/03/11/large_Sat-Isabgol-100G-Pran.jpeg"""},
                        {"name" : "Hot Oil Hair Mask- Blackseed 500g Vatika", "price" : '20.00$',  'img':"""/media/img/2023/03/11//large_vatika-blackseed-multivitamin-hair-mask-grande.png"""},

                
                        {"name" : "Blackseed Multivitamin+ Hair Oil 200ml Vatika Dabur", "price" : '19.00$',  'img':"""/media/img/2023/03/11/large_vatika-naturals-blackseed-multivitamin-hair-oil-grande.png"""},
                        {"name" : "Vatika Naturals Cactus Hair Oil 200ml", "price" : '10.00$',  'img':"""/media/img/2023/03/11/large_vatika-naturals-cactus-multivitamin-hair-oil-grande.png"""},
                        {"name" : "Idiyappam Powder  500G Aachi", "price" : '5.00$',  'img':"""/media/img/2023/03/11/large_Kozhukattai-1000x1000.png"""},
                        {"name" : "Saffola Masala oats,40g", "price" : '3.00$',  'img':"""/media/img/2023/03/11/large_Saffola-Masala-Oats-Classic-Masala40g..jpg"""},

                        {"name" : "Rice Dosa Mix Aachi 1kg", "price" : '12.00$',  'img':"""/media/img/2023/03/11/large_Rice-dosa.jpg"""},
                        {"name" : " Sugar Coated Fennel Seed 250G Little India", "price" : '7.00$',  'img':"""/media/img/2023/03/11/large_moti.png"""},
                        {"name" : "Vimal Pan Masala V-1Tobacco", "price" : '80.00$',  'img':"""/media/img/2023/03/11/large_Vimal.jpg"""},
                        {"name" : "Vicco Vajradanti Tooth Powder 50g", "price" : '2.00$',  'img':"""/media/img/2023/03/11/large_Vicco-Proszek-do-Czyszczenia-Zebow-i-Dziasel-50g.jpg"""},

                        {"name" : "Mint Chutney 190G Ashoka", "price" : '5.00$',  'img':"""/media/img/2023/03/11/large_Bez-nazwy.png"""},
                        {"name" : "Schezwan Chutney (with olive oil) 190g Ashoka", "price" : '5.00$',  'img':"""/media/img/2023/03/11/large_landscape-white-bg-shadow-designify-29-.png"""},
                        {"name" : "Samosa Chutney 410G Suhana", "price" : '8.00$',  'img':"""/media/img/2023/03/11/large_WhatsApp-Image-2021-05-09-at-13-00-54.jpeg"""},
                        {"name" : "Sandwich Chutney 190G Ashoka", "price" : '9.00$',  'img':"""/media/img/2023/03/11/large_Bez-nazwy.png"""},

                        {"name" : "Ridge Gourd Beerakaaya Chutney 100g Priya", "price" : '4.00$',  'img':"""/media/img/2023/03/11/large_61jgtbrcQHL-SX679-.jpg"""},
                        {"name" : "Coconut milk - 12 x 400g", "price" : '65.00$',  'img':"""/media/img/2023/03/11/large_mleko-kokosowe.jpg"""},
                        {"name" : "Pudina Chana 400g Little India", "price" : '7.00$',  'img':"""/media/img/2023/03/11/large_WhatsApp-Image-2022-07-29-at-15-35-19.jpeg"""},
                        {"name" : "Tapioca Chips Classic Salt 160g A-1 Chips", "price" : '3.00$',  'img':"""/media/img/2023/03/11/large_Tapiaco-Chips-Classic-Salt.jpg"""},

                        {"name" : "Tapioca Chips Salsa Masala 160g A-1 Chips", "price" : '4.00$',  'img':"""/media/img/2023/03/11/large_1069-12-2015-A1-chips-Tapioca-Chips-Salsa-Masala.jpg"""},
                        {"name" : "Tapioca Chips Classic Salt 160g A-1 Chips", "price" : '13.00$',  'img':"""/media/img/2023/03/11/large_35-24a557aa-1963-4550-9d19-02c6f3ac2552-1-.png"""},
                        {"name" : "Gentle Baby Wash HIMALAYA 200ml", "price" : '20.00$',  'img':"""/media/img/2023/03/11/large_Himalaya-Gentle-Baby-Wash-200ml.jpg"""},
                        {"name" : "Vadu Mango Pickle Aachi 300g", "price" : '10.00$',  'img':"""/media/img/2023/03/11/large_pobrane.jpeg"""},

                        {"name" : "Sweet Mango Pickle (with peeled) 500g Rasanand", "price" : '7.00$',  'img':"""/media/img/2023/03/11/large_portrait-white-bg-shadow-designify.png"""},
                        {"name" : "Ahmed Mango Pickle in oil 330g/400g/1kg", "price" : '19.00$',  'img':"""/media/img/2023/03/11/large_big-Ahmed-Mangopickle.jpg"""},
                        {"name" : "Pav Bhaji - 280g Ashoka", "price" : '3.00$',  'img':"""/media/img/2023/03/11/large_Bombay-Pav.jpg"""},
                        {"name" : "Rajma Pulao 280G Ashoka", "price" : '8.00$',  'img':"""/media/img/2023/03/11/large_ashoka-rajma-pulao-1.jpg"""},
                        ],
               
                }
                items_name = products_names.objects.all()
                length = len(data["items"])
                for i in range(length):
                         if len(items_name) == 0:
                                
                                print(data['items'][i]['name'])
                                items_insert = products_names(item_name = data['items'][i]['name'], price = data['items'][i]['price'], item_img =  data['items'][i]['img'] )
                                items_insert.save()
                                r = commonData()
                view = products_names.objects.all()
                
                                


                

                return render(request,"shop.html",{'view':view})
        def register(request):
                
                return render(request,'register.html')
        
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
                                        send_email()
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
                                        send_email()
                                        return render(request,'login.html')
                        except:
                                return render(request,'login.html')
                return render(request,'login.html')
        def user(request):
                if request.method == "POST":
                        login_email = request.POST.get('login_email')
                        login_password = request.POST.get('login_password')
                        register_email = request.POST.get('email')
                        register_password = request.POST.get('password')
                        user= register.objects.values_list('Email_ID',flat=True)
                        user1 = register.objects.values_list('password',flat=True)
                        #user1 = authenticate(request,Email_ID=login_email, password= login_password )
                        l = len(user)
                        for i in range(l):
                                for j in range(i+1):
                                        if user[i] == login_email and user1[i] == login_password:
                                                d = register.objects.get(Email_ID = login_email)
                                                return render(request,'user.html',{'data':d})
                                        break
                        messages.error(request,"EMAIL ID OR PASSWORD IS INCORRECT")
                        return redirect('login')

                        
                
                       
               
        @api_view()
        def api(request):
                return Response({'status' : 200 , 'message':'this is my first api framework'})
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 
        

        
                
               
               



