from django.urls import path
from users.views import login,logout,profile,register,cart_user

app_name ="users"

urlpatterns=[
    path('login/', login , name="login"),
    path('inscription/',register,name="register"),
    path('profil/',profile,name="profile"),
    path('panier-utilisateur/',cart_user,name="cart-user"),
    path('logout/',logout,name="logout"),
]