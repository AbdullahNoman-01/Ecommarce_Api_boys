from django.db import models

# Create your models here.

# Category Model
class Category(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
       return self.name
   
# Brand Model
class Brand(models.Model):
   name = models.CharField(max_length=100)
   def __str__(self):
       return self.name

# Product Model
STOCK_STATUS = (
    ('in_stock', 'In Stock'),
    ('out_of_stock', 'Out of Stock'),
    ('low_stock', 'Low Stock'),
)

class Product(models.Model):
   name = models.CharField(max_length=20)
   discription = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   stock_status = models.CharField(choices=STOCK_STATUS,default='in_stock')

   #relationship
   category = models.ForeignKey(Category,on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

   image = models.ImageField(upload_to='product/images/')
   created_up = models.DateTimeField(auto_now_add=True)


   def __str__(self):
       return self.name
   
class SummarCollection(models.Model):
    name = models.CharField(max_length=30)
    discription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/photo/",)
    created_up = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock_status = models.CharField(choices=STOCK_STATUS,default='in_stock')
    
    def __str__(self):
       return self.name