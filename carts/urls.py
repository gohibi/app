from django.urls import path
from carts import views

app_name= "carts"

urlpatterns = [
    path('ajouter-au-panier/<str:pid>/',views.add_cart , name="add-cart"),
    path('modifier-panier/<str:pid>/',views.change_cart,name="change-cart"),
    path('supprimer-panier/<int:cart_id>/',views.remove_cart,name="remove-cart")
]