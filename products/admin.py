from django.contrib import admin
from .models import Category , Product

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}

@admin.register(Product)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
        'quantity',
        'category',
        'product_image'
    ]