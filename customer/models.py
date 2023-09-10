from django.db import models
from seller.models import Products
# Create your models here.
class Customer(models.Model):
    customer_name=models.TextField(max_length=50,db_column="cust_name")
    customer_dob=models.DateField(db_column="cust_dob")
    customer_address=models.TextField(max_length=200,db_column="cust_address")
    customer_mobile=models.TextField(max_length=10,db_column="cust_mobile")
    customer_email=models.TextField(max_length=50,db_column="cust_email")
    customer_password=models.TextField(max_length=20,db_column="cust_password")
    customer_gender=models.TextField(max_length=10,db_column="cust_gender")
    otp=models.TextField(max_length=10,db_column="otp",null=True)
    status=models.TextField(max_length=50,db_column="status",default="",null=True)
    
    
    class Meta:
        db_table="customer"
    
class Orders(models.Model):
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    quantity= models.IntegerField(db_column="quantity") 
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    status=models.TextField(max_length=20,db_column="status") 
    
    class Meta:
        db_table="orders"