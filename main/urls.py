from django.urls import path
from main.views import indexView , AboutView

app_name ='main'

urlpatterns = [
    path('',indexView.as_view(),name="index"),
    path('about-us/',AboutView.as_view(), name="about")
]