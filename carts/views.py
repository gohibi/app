from django.shortcuts import render,redirect
from products.models import Product
from users.models import User
from carts.models import Cart

# Create your views here.

def add_cart(request,pid):
    product = Product.objects.get(pid=pid)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user , product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity +=1
                cart.save()
        else:
            Cart.objects.create(user=request.user , product = product , quantity = 1)
            
    return redirect(request.META['HTTP_REFERER'])


def change_cart(request,pid):
    pass

def remove_cart(request,pid):
    pass