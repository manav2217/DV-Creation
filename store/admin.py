from django.contrib import admin
from .models.catagory import Catagory
from .models.customer import Customer
from .models.product import Product
from .models.orders import Order
from .models.contact import Contact

class Adminproduct(admin.ModelAdmin):
    list_display = ['p_name' , 'catagory' , 'price']
    
class AdminOrder(admin.ModelAdmin):
    list_display = ['user_id' , 'customer_email' , 'product' , 'price' , 'quantity']
    
class Admincontact(admin.ModelAdmin):
    list_display = ['email' , 'subject']

# Register your models here.

admin.site.register(Catagory)
admin.site.register(Customer)
admin.site.register(Product , Adminproduct)
admin.site.register(Order , AdminOrder)
admin.site.register(Contact , Admincontact)
