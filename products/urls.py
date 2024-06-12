from django.urls import path
from products import views


app_name="products"

urlpatterns = [
    path('',views.Catalog,name="catalog"),
    path('produits/',views.Product, name="product"),
    path('category/product/<str:slug>',views.product_category,name="product-category")
]