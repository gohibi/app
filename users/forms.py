from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm

class Loginform(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
        "autofocus": True ,
        "class":"form-control",
        "placeholder":"Entrez votre nom d'utilisateur",
                                                             
    }))
    password = forms.CharField(
            label="Mot de passe",
            widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class":"form-control",
            "placeholder":"Tapez votre mot de passe"
        
    }))
    class Meta:
        model = User
        fields = ['username','password']
        