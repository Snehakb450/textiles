from django.shortcuts import render,redirect
from . models import Sellers,Products
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def seller_login(request):   
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pwd']
        
        try :      
            seller=Sellers.objects.get(resel_email=username,pwd=password)
            request.session['seller_id'] =seller.id   
            if seller.rstatus=='active':     
                return redirect('seller:seller_product') 
        except Sellers.DoesNotExist:
            return render(request,"seller/seller_login.html",{'message': 'login failed'})
    return render(request,'seller/seller_login.html')

def seller_signup(request):
    message=""
    if request.method=="POST":
            companyname=request.POST['resellercompanyname']
            companyid=request.POST['resellercompanyid']
            address=request.POST["address"]
            mobile=request.POST["mobile"]
            email=request.POST["email"] 
            account_name=request.POST['resellerbankaccountname']
            account_number=request.POST['resellerbankaccountnumber']
            account_ifsc=request.POST['resellerbankaccountifsc']
            reseller_exist=Sellers.objects.filter(resel_email=email).exists()
            if not reseller_exist :
                otp=randint(100000,999999)
                send_mail(
                    'Please verify your otp',
                    'This is your password . login using theis otp and you can change the password'+  str(otp),
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                resel=Sellers(resel_company_name=companyname,resel_company_id=companyid,resel_address=address,
                resel_mobile=mobile,resel_email=email,resel_accountholder_name=account_name,
                resel_account_number=account_number,resel_ifsc_number=account_ifsc,pwd=str(otp),rstatus='to_verify')
                resel.save()
                seller_data=Sellers.objects.get(resel_email=email)
                request.session['seller_id']=seller_data.id 
                return redirect('seller:seller_login')
            else:
                message="Reseller already exist"
                    
   
    return render(request,'seller/seller_signup.html', {'mse':message})

def seller_master(request):
    return render(request,'seller/seller_master.html') 

def seller_add(request):
    if request.method == 'POST':
        seller_id=request.session['seller_id']  
        title =request.POST['title']
        regproductid= request.POST['regproductid'] 
        description= request.POST['description']       
        price= request.POST['price']
        quantity = request.POST['quantity']
        weight= request.POST['weight']
        weightunit = request.POST['weightunit']     
        brand=request.POST['brand']
        status = request.POST['status']        

        if len(request.FILES)!=0 :
            image=request.FILES['image']
        
        product = Products(title=title, reg_productid=regproductid, desc=description,img=image, 
                            price=price, quantity =quantity, weight=weight, weightunit=weightunit
                            ,brand=brand,resel_id_id=seller_id,status=status)  
        product.save()   
        return redirect('seller:seller_product') 
    
    
    return render(request,'seller/seller_add.html') 

def seller_product(request):
    loginid = request.session['seller_id']  
    sellerid = Sellers.objects.get(id=loginid) 
    products = Products.objects.filter(resel_id_id=sellerid) 
    
    return render(request,'seller/seller_product.html',{'products':products}) 

def seller_change(request):
    if request.method=='POST':       
          current_pwd=request.POST['pwd9']
          new_pwd=request.POST['pwd10']
          seller_id=request.session['seller_id']  
          data=Sellers.objects.get(id=seller_id)
          if current_pwd==data.pwd :
               Sellers.objects.filter(id=seller_id).update(pwd=new_pwd)
               return redirect('seller:seller_product')
         
    return render(request,'seller/seller_change.html') 

def logout(request):
    del request.session['seller_id']
    return redirect('seller:seller_login') 

def edit_product(request,s_id):
    if request.method == 'POST':
           
        title =request.POST['title']
        regproductid= request.POST['regproductid'] 
        description= request.POST['description']       
        price= request.POST['price']
        quantity = request.POST['quantity']
        weight= request.POST['weight']
        weightunit = request.POST['weightunit']   
        brand=request.POST['brand']
        status = request.POST['status']        
        
        Products.objects.filter(id=s_id).update(title=title, reg_productid=regproductid, desc=description, 
                            price=price, quantity =quantity, weight=weight, weightunit=weightunit,                           
                            brand=brand,status=status) 
        return redirect('seller:seller_product') 
    else:
        data=Products.objects.get(id=s_id) 
    
    return render(request,'seller/edit_product.html',{'data':data})  
    
def delete_product(request,s_id):
    Products.objects.get(id=s_id).delete()   
    return redirect('seller:seller_product')
 
def forgot(request):
    mes=""
    if request.method=='POST':
          mail=request.POST['emailorUsername']
          seller_exist=Sellers.objects.filter(resel_email=mail).exists()
          a=Sellers.objects.get(resel_email=mail) 
          if not seller_exist:
               mes="You don't have an account." 
          
          else:
               sotp=randint(1000,9999)
               send_mail('Please verify yout otp',
                         'Login with this otp and change your password'+str(sotp),
                         settings.EMAIL_HOST_USER,
                         [mail],fail_silently=False,
               )
               
               Sellers.objects.filter(id=a.id).update(pwd=str(sotp))
               return redirect('seller:seller_login') 
           
    return render(request,'seller/forgot.html')   