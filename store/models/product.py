from django.db import models

from .catagory import Catagory


class Product(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/" , default="abc")
    
    def __str__(self):
        return self.p_name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_catagory_id(catagory_id):
        if catagory_id:
            return Product.objects.filter(catagory = catagory_id)
        else:
            return Product.get_all_products()
        
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
    
    
    