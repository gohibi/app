from django.urls import path
from products import views


app_name="products"

urlpatterns = [
    path('<slug:category_slug>/',views.catalog,name="catalog"),
    path('recherche/',views.catalog,name="search"),
    path('produit/details/<slug:slug>/<str:pid>',views.product_detail, name="product-detail"),
   
]