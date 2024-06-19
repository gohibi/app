from django.urls import path
from users.views import login,logout,profile,register

app_name ="users"

urlpatterns=[
    path('login/', login , name="login"),
    path('inscription/',register,name="register"),
    path('profil/',profile,name="profile"),
    path('logout/',logout,name="logout"),
]