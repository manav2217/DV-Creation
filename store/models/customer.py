from django.db import models
import random
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField(null=True , blank=True)
    password = models.CharField(max_length=5000)
    otp = models.IntegerField(default=None , blank=True , null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
    @staticmethod
    def get_customer(customer_email):
        return Customer.objects.get(email=customer_email)
    
       
            
    
    