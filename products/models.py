from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150 ,  unique= True)
    slug = models.SlugField(max_length=200,unique=True,blank=True, null=True , verbose_name='URL')
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            value = self.name
            self.slug =slugify(value,allow_unicode=True)
        return super().save(*args,**kwargs)
    
class Product(models.Model):
    pid = ShortUUIDField(length=10, max_length=15 , prefix="PROD", alphabet="0123456789")
    name = models.CharField(max_length=150 ,  unique= True)
    slug = models.SlugField(max_length=200,unique=True,blank=True, null=True , verbose_name="URL")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="img/",blank=True, null=True )
    price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name="Prix")
    old_price = models.DecimalField(max_digits=10,decimal_places=0 ,verbose_name="Ancien prix",blank=True,null=True)
    quantity = models.PositiveIntegerField(default="0",verbose_name="Quantité")
    category = models.ForeignKey(on_delete=models.CASCADE, to=Category, related_name="category")
    
    class Meta:
        verbose_name_plural = "Products"
        ordering =['category']
    
    def product_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50">')
        return "No image"
        
    
    def get_discount(self):
        if self.old_price > 0:
            discount = (self.price / self.old_price) * 100
            return discount
        return 0
    
    def __str__(self):
        return self.name 
        
    def save(self,*args,**kwargs):
        if not self.slug:
            value = self.name
            self.slug =slugify(value,allow_unicode=True)
        return super().save(*args,**kwargs)
        
    
    