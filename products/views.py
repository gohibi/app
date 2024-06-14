from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from products.models import Product, Category


# def catalog(request):
#     context={}
    

#     on_sale = request.GET.get('on_sale',None)
#     order_by = request.GET.get('order_by',None)
    
#     product_list = Product.objects.all()
#     items_per_page = 3
#     paginator = Paginator(product_list,items_per_page)
#     page_number = request.GET.get('page')
#     products = paginator.get_page(page_number)
    
#     if on_sale:
#         products = product_list.filter(old_price__isnull=True)
#     if order_by and order_by != "default":
#         products =product_list.order_by(order_by)
    
    
#     context['products'] = products
    
#     return render(request,'products/catalog.html' , context)
def catalog(request,category_slug , page=1):
    context={}
    if category_slug == "all":
        products = Product.objects.all()
        catname = "Tous les produits"
    else:
        category =get_object_or_404(Category,slug=category_slug)
        products = get_list_or_404(Product.objects.filter(category = category))
        catname = category.name
        
    nbr_items = 3
    paginator =Paginator(products,nbr_items)
    current_page = paginator.page(page)
    
    context["products"] = current_page
    context['catname'] = catname
    context["slug_url"] = category_slug
    
    return render(request,'products/catalog.html' , context)




# def product_category(request,slug):
#     context={}
#     categorie = Category.objects.get(slug=slug)
#     products = Product.objects.filter(category=categorie)
#     context['categorie'] = categorie
#     context['products'] = products
#     return render(request,'products/product-category.html',context)

def product_detail(request,slug,pid):
    product = get_object_or_404(Product,slug=slug,pid=pid)
    context = {
        'prod':product
    }
    return render(request,'products/product.html',context)


