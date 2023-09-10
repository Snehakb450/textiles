from django.db import models

# Create your models here.

class Sellers(models.Model):
    resel_company_name=models.TextField(max_length=50,db_column="companyname")
    resel_company_id=models.TextField(max_length=20,db_column="companyid")
    resel_address=models.TextField(max_length=200,db_column="address")
    resel_mobile=models.TextField(max_length=10,db_column="mobile")
    resel_email=models.TextField(max_length=30,db_column="email")
    resel_accountholder_name=models.TextField(max_length=50,db_column="holder_name")  
    resel_account_number=models.TextField(max_length=50,db_column="accountnumber")
    resel_ifsc_number=models.TextField(max_length=30,db_column="ifsc")
    pwd=models.TextField(max_length=10,db_column="pwd",null=True)
    rstatus=models.TextField(max_length=50,db_column="status",default="",null=True) 
    
 
    
    class Meta:
        db_table="sellers"

class Products (models.Model):
    resel_id=models.ForeignKey(Sellers,on_delete=models.CASCADE,null=True) 
    title = models.TextField(max_length=30,db_column="product_title")
    reg_productid= models.TextField(max_length=12,db_column="product_id")
    desc= models.TextField(max_length=200,db_column="desc")
    img = models.ImageField(upload_to='product_images/', blank=True, null=True, db_column="image") 
    price = models.IntegerField(db_column="price")
    quantity= models.IntegerField(db_column="quantity") 
    weight = models.IntegerField(db_column="weight")
    weightunit = models.CharField(max_length=12,db_column="wieghtunit")
    brand=models.CharField(max_length=20,db_column="brand",default="")  
    status = models.CharField (max_length=100,db_column="status")
    
    class Meta:
        db_table="products" 
    

        