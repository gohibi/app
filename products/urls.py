from django.urls import path
from products import views


app_name="products"

urlpatterns = [
    path('<slug:category_slug>/',views.catalog,name="catalog"),
    path('<slug:category_slug>/<int:page>',views.catalog,name="catalog"),
    path('produit/details/<slug:slug>/<str:pid>',views.product_detail, name="product-detail"),
    # path('categorie/produit/<slug:slug>',views.product_category,name="product-category")
]