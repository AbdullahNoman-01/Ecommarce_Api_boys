from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = (
   ('pending','pending'),
   ('processing', 'Processing'),
   ('shipped', 'Shipped'),
   ('delivered', 'Delivered'),
   ('cancelled', 'Cancelled'),
)

class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total_price = models.DecimalField(max_digits=10, decimal_places=3)
   status = models.CharField(choices= STATUS_CHOICES, default= "pending")
   address = models.TextField()

   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"Order: #{self.id} - {self.user.username}" 
   