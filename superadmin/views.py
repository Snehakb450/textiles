from django.shortcuts import render,redirect
from .models import Data
from seller.models import Sellers
from django.http import JsonResponse
from customer.models import Customer
from random import randint
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def get_admin_master(request):
    return render(request,'superadmin/admin_master.html') 

def dashboard(request):
    sellers=Sellers.objects.count()
    customers=Customer.objects.count() 
    seller=Sellers.objects.all()
    customer=Customer.objects.all()
    
    return render(request,'superadmin/dashboard.html',{'sellers':sellers,'customers':customers,'seller':seller,'customer':customer})   

def add_seller(request):
    reqdata=Sellers.objects.all()
    
    return render(request,'superadmin/add_seller.html',{"userrequests":reqdata}) 

def admin_change(request):
    if request.method=='POST':       
          current_pwd=request.POST['pwd9']
          new_pwd=request.POST['pwd10']
          super_id=request.session['admin_id']  
          data=Data.objects.get(id=super_id)
          if current_pwd==data.password :
               Data.objects.filter(id=super_id).update(password=new_pwd)
               return redirect('superadmin:dashboard')
         
    return render(request,"superadmin/admin_change.html")

def logout(request):
    del request.session['admin_id']
    return redirect('superadmin:admin_login') 

def admin_login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pwd']
        
        try :      
            admin=Data.objects.get(username=username,password=password)
            request.session['admin_id'] =admin.id         
            return redirect('superadmin:dashboard') 
        except Data.DoesNotExist:
            return render(request,"superadmin/admin_login.html",{'message': 'login failed'})
    return render(request,'superadmin/admin_login.html')

def deleteseller(request,a_id):
    Sellers.objects.get(id=a_id).delete()
    return redirect ('superadmin:add_seller')  

def update_seller_status(request):
    if request.method == 'POST':
        seller_id = request.POST.get('adminId')
        status = request.POST.get('status')
        
        # Assuming you have a model called 'Staff' with a field 'status' to store the admin status
        try:
            seller = Sellers.objects.get(id=seller_id)
            seller.rstatus = status
            seller.save()
            return JsonResponse({'success': True})
        except Sellers.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Seller not found'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def forgot(request):
    mes=""
    if request.method=='POST':
          mail=request.POST['emailorUsername']
          admin_exist=Data.objects.filter(username=mail).exists()
          a=Data.objects.get(username=mail) 
          if not admin_exist:
               mes="You don't have an account." 
          
          else:
               sotp=randint(1000,9999)
               send_mail('Please verify yout otp',
                         'Login with this otp and change your password'+str(sotp),
                         settings.EMAIL_HOST_USER,
                         [mail],fail_silently=False,
               )
               
               Data.objects.filter(id=a.id).update(password=str(sotp))
               return redirect('superadmin:admin_login') 
           
    return render(request,'superadmin/forgot.html')   

def home(request):
    return render(request,'superadmin/home.html') 

