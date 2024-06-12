from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from products.models import Product, Category


def Catalog(request):
    context={}
    context['products'] = Product.objects.all()
    return render(request,'products/catalog.html' , context)

def product_category(request,slug):
    context={}
    categorie = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=categorie)
    context['categorie'] = categorie
    context['products'] = products
    return render(request,'products/product-category.html',context)

