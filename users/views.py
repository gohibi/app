from django.shortcuts import render , redirect
from users.forms import Loginform , RegisterForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def login(request):
    context={}
    if request.method == "POST":
        form = Loginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username , password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = Loginform()        
       
    context['title'] = "Authentification"
    context['form'] = form
    return render(request,'users/login.html',context)



def register(request):
    context={} 
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.instance
            auth.login(request,user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = RegisterForm()
    
    context['title'] ="Inscription"
    context['form'] = form
    return render(request,'users/register.html',context)




def profile(request):
    context={}
    context['title'] = "Profil de l'utilisateur"
    return render(request,'users/profile.html',context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))