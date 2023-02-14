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

                
                try:
                       
                       if request.method == 'POST':
                                first_name = request.POST.get("first_name")
                                last_name = request.POST.get("last_name")
                                phone_number = request.POST.get("phone_number")
                                email = request.POST.get("email")
                                password = request.POST.get("password")
                                re_password = request.POST.get("re-password")
                except:
                      pass
              
                

                return render(request,'register.html')
        def login(request):
               r = commonData()
               if request.method == 'POST':
                        first_name = request.POST.get("first_name")
                        return render(request,"login.html",r.data)
               return render(request,"login.html",r.data)
              
               
               


    


