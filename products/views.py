from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import PageNotAnInteger , EmptyPage ,Paginator
from products.models import Product, Category


def catalog(request):
    context={}
    product_list = Product.objects.all()
    items_per_page = 3
    paginator = Paginator(product_list,items_per_page)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context['products'] = products
    return render(request,'products/catalog.html' , context)

def product_category(request,slug):
    context={}
    categorie = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=categorie)
    context['categorie'] = categorie
    context['products'] = products
    return render(request,'products/product-category.html',context)

def product_detail(request,slug,pid):
    product = get_object_or_404(Product,slug=slug,pid=pid)
    context = {
        'prod':product
    }
    return render(request,'products/product.html',context)