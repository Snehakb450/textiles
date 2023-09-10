from django.shortcuts import render,redirect
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from . models import Customer,Orders
from seller.models import Sellers,Products
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def get_customer_home(request):
    return render(request,'customer/customer_home.html') 

def get_customer_master(request):
    return render(request,'customer/customer_master.html') 

def signup(request):
    message="" 
    if request.method=="POST":       
            name=request.POST['firstname']
            gender=request.POST['gender']
            dob=request.POST['dateofbirth']
            address=request.POST["address"]
            mobile=request.POST["mobile"] 
            email=request.POST["email"] 
            password=request.POST["password"]            
            customer_exist=Customer.objects.filter(customer_email=email).exists()
            if not customer_exist :
                otp=randint(1000,9999)
                send_mail('Please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [email], 
                )
                cust=Customer(customer_name=name,customer_gender=gender,customer_dob=dob,customer_address=address,
                              customer_mobile=mobile,customer_email=email,customer_password=password,otp=str(otp),status='to_verify')  
                cust.save()
                customer_data=Customer.objects.get(customer_email=email)
                request.session['customer_id']=customer_data.id
                
                return redirect('customer:login') 
            else:
                message="Customer already exist"
    return render(request,'customer/signup.html') 

def verify_otp(request):
    if request.method=="POST":
        otp=request.POST['otp']
        c_id=request.session['customer_id']
        data=Customer.objects.get(id=c_id)
        if otp==data.otp:
            Customer.objects.filter(id=c_id).update(status='active')
            return redirect('customer:login')
        else:
            return render(request,"customer/verify_otp.html",{ 'mes':'invalid otp'})
    return render(request,"customer/verify_otp.html")
    
def login(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pwd']
        
        try :      
            customer=Customer.objects.get(customer_email=username,customer_password=password)
            request.session['customer_id'] =customer.id         
            return redirect('customer:customer_home') 
        except Customer.DoesNotExist:
            return render(request,"customer/login.html",{'message': 'login failed'})
    
    return render(request,'customer/login.html')  

def customer_profile(request):
    if 'customer_id' in request.session:
        c_id=request.session['customer_id']
        customer_details=Customer.objects.get(id=c_id) 
        
        return render(request,"customer/customer_profile.html",{ 'data': customer_details}) 
    else:
        return redirect('customer:login')

def edit_profile(request,c_id):
    if request.method=='POST':
        name=request.POST['firstname']
        address=request.POST['address']
        email=request.POST['mail'] 
        mobile=request.POST['mobile']

        Customer.objects.filter(id=c_id).update(customer_name=name,customer_address=address,customer_email=email,customer_mobile=mobile)
        return redirect('customer:customer_profile')  
    else:
        data=Customer.objects.get(id=c_id)
        return render (request,"customer/edit_profile.html",{'data':data}) 

def change(request):
    if request.method=='POST':       
          current_pwd=request.POST['pwd9']
          new_pwd=request.POST['pwd10']
          customer_id=request.session['customer_id']  
          data=Customer.objects.get(id=customer_id)
          if current_pwd==data.customer_password:
               Customer.objects.filter(id=customer_id).update(customer_password=new_pwd)
               return redirect('customer:customer_profile')
    return render(request,'customer/change.html') 

def view_cart(request):
    bagdata = Orders.objects.all()
    # Create an empty list to hold the productdata for each bag item
    productdata = []

    for order in bagdata:
        # Get the productdata for each bag item and append it to the list
        product = Products.objects.get(id=order.product_id_id)
        productdata.append(product)
        
    return render(request, "customer/view_cart.html", {'bagdata': bagdata, 'productdata': productdata})


def logout(request):
    del request.session['customer_id']
    return redirect('customer:login')  

def view_product(request,id):
    productdetails=Products.objects.get(id=id) 
    return render (request, "customer/view_product.html", {"productdata": productdetails})
    

def search_product(request):
    if request.method == "POST":
        search_word = request.POST['searchdata']
        search_list = search_word.split(' ')
        print(search_list)

        srch_products = Products.objects.filter(
            Q(title__icontains=search_word) |
            Q(brand__icontains=search_word),
            status='Active'
        )

        print(srch_products)
        # Rendering search product page
        return render(request, "customer/search_product.html", {'search_products': srch_products})
    return render(request, "customer/search_product.html") 

def add_to_bag(request):
    try:
        quantity = request.POST['quantity']
        product_id = request.POST['product_id']
        cust_id = request.session['customer_id']
        
        orderdata = Orders(product_id_id=product_id, quantity=quantity, customer_id_id=cust_id, status='added_to_bag')
        orderdata.save()
        return JsonResponse({"status": "success"})
    except KeyError:
        return JsonResponse({"status": "error"})


def remove(request,p_id):
    data=Orders.objects.get(product_id=p_id).delete()
    return redirect('customer:view_cart') 

def forgot(request):
    mes=""
    if request.method=='POST':
          mail=request.POST['emailorUsername']
          customer_exist=Customer.objects.filter(customer_email=mail).exists()
          a=Customer.objects.get(customer_email=mail) 
          if not customer_exist:
               mes="You don't have an account." 
          
          else:
               sotp=randint(1000,9999)
               send_mail('Please verify yout otp',
                         'Login with this otp and change your password'+str(sotp),
                         settings.EMAIL_HOST_USER,
                         [mail],fail_silently=False,
               )
               
               Customer.objects.filter(id=a.id).update(customer_password=str(sotp))
               return redirect('customer:login') 
           
    return render(request,'customer/forgot.html')   

