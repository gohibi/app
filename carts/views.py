from django.shortcuts import render

# Create your views here.

def add_cart(request,pid):
    context={}
    return render(request,"carts/add_cart.html",context)


def change_cart(request,pid):
    pass

def remove_cart(request,pid):
    pass