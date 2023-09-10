from django.db import models

# Create your models here.
class Data(models.Model):
    username=models.CharField(max_length=20,db_column="username")
    password=models.CharField(max_length=20,db_column="password")
    
    class Meta:
        db_table="data"
        
        