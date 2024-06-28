from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    # Basic information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Phone_number = models.CharField(max_length=15)
    
    # Additional information
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    image=models.ImageField(blank=True,null=True,)
    
    # Employment details
    date_hired = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.first_name
    

class User(AbstractUser):
     college=models.CharField(max_length=20,null=True,blank=True)
     age=models.IntegerField(null=True,blank=True)

        