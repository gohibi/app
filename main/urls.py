from django.urls import path
from main.views import indexView
app_name ='main'

urlpatterns = [
    path('',indexView.as_view(),name="index")
]