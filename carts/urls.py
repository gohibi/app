from django.urls import path
from carts import views

app_name= "carts"

urlpatterns = [
    path('ajouter-au-panier//',views.add_cart , name="add-cart"),
    path('modifier-panier/',views.change_cart,name="change-cart"),
    path('supprimer-panier/',views.remove_cart,name="remove-cart")
]