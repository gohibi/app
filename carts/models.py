from django.db import models
from users.models import User
from products.models import Product , Category
# Create your models here.

class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.product_sell() for cart in self)
    
    def total_item(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    

class Cart(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    at_created = models.DateTimeField(auto_now_add=True)
    key_session = models.CharField(max_length=32,blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Carts"
        
    objects = CartQueryset().as_manager() 
        
    def product_sell(self):
        return round(self.product.price * self.quantity, 0)
    
    def __str__(self):
        return f"Cart {self.user.username} | product {self.product.name} | quantity {self.quantity}"