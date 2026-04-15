from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Review(models.Model):
   RATING_CHOICES = (
      ('⭐', '⭐'),
      ('⭐⭐', '⭐⭐'),
      ('⭐⭐⭐', '⭐⭐⭐'),
      ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
      ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
   )
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
   rating = models.CharField(choices=RATING_CHOICES)
   comment = models.TextField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
      constraints = [
         models.UniqueConstraint(fields=['user', 'product'], name='unique_user_product_review')
      ]

   def __str__(self):
      return f"{self.user.username} - {self.product.name} ({self.rating})"