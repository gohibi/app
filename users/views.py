from django.shortcuts import render , redirect
from users.forms import Loginform , RegisterForm , Profileform
from django.contrib import auth , messages
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required 

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
                messages.success(request , f"{username} , vous etes connectés")
                
                redirect_page  = request.POST.get("next",None)
                
                if redirect_page and redirect_page != reverse("users:logout"):
                    return HttpResponseRedirect(request.POST.get('next'))
                
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
            messages.success(request,f"{user.username} vous etes inscrit avec succès & connectés à votre compte ")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = RegisterForm()
    
    context['title'] ="Inscription"
    context['form'] = form
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    context={}
    if request.method == "POST":
        form = Profileform(request.POST , instance = request.user , files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mis a jour du profil avec succès")
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = Profileform(instance=request.user)
    context['form'] = form
    context['title'] = "Profil de l'utilisateur"
    return render(request,'users/profile.html',context)

def cart_user(request):
    return render(request,'users/cartuser.html')


@login_required
def logout(request):
    messages.warning(request,f"{request.user.username} , Vous etes deconnectés avec succes!")
    auth.logout(request)
    return redirect(reverse('main:index'))