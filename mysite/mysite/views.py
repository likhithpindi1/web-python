from django.http import HttpResponse
from django.shortcuts import render

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
                r = commonData()
                return render(request,"register.html",r.data)


    


