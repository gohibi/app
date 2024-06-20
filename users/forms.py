from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class Loginform(AuthenticationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
        "autofocus": True ,
        "class":"form-control",
        "placeholder":"Entrez votre nom d'utilisateur",
        "id":"id_username"
                                                             
    }))
    password = forms.CharField(
            label="Mot de passe",
            widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class":"form-control",
            "placeholder":"Tapez votre mot de passe",
            "id":"id_password"
        
    }))
    class Meta:
        model = User
        fields = ['username','password']
        
        
        
        

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="Prenoms",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Entrez votre prenom',
                'id':'id_first_name'
            }
        )
    )
    
    last_name = forms.CharField(
        label="Nom de famille",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Entrez votre nom de famille',
                'id':'id_last_name'
            }
        )
    )
    
    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
        "autofocus": True ,
        "class":"form-control",
        "placeholder":"Entrez votre nom d'utilisateur",
        'id':'id_username',
                                                             
    }))

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "autofocus": True ,
                "class":"form-control",
                "placeholder":"Entrer votre Email",
                'id':'id_email',
            }
        )
        
    )
    
    password1 = forms.CharField(
        label = "Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder":"Entrer le mot de passe",
            "class":"form-control",
            'id':'id_password1',
            
    }))
    password2 = forms.CharField(
        label = "Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder":"Confirmez le mot de passe",
            "class":"form-control",
            'id':'id_pasword2',
            
    }))

    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']