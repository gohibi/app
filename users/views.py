from django.shortcuts import render

# Create your views here.

def login(request):
    context={}
    context['title'] = "Authentification"
    return render(request,'users/login.html',context)

def register(request):
    context={}
    context['title'] ="Inscription"
    return render(request,'users/register.html',context)

def profile(request):
    context={}
    context['title'] = "Profil de l'utilisateur"
    return render(request,'users/profile.html',context)

def logout():
    pass