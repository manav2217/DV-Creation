from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    customer_email = models.EmailField(max_length=254 , default='' , blank=True)
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50 , default='')
    state = models.CharField(max_length=50 , default='')
    city = models.CharField(max_length=50 , default='')
    street = models.CharField(max_length=50, default='')
    pincode = models.IntegerField(default=123456)
    address = models.CharField(max_length = 100 , default='')
    phone = models.CharField(max_length = 20, default='')
    price = models.IntegerField(default=0)
    date = models.DateField( default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    
    @staticmethod
    def get_order_by_id(customer_id):
        return Order.objects.filter(user_id = customer_id)
    
    @staticmethod
    def get_orders(order_id):
        return Order.objects.filter(id=order_id)