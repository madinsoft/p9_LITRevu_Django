"""from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        widgets = {
            'password1': forms.HiddenInput,  # Cachez le champ du mot de passe
            'password2': forms.HiddenInput,  # Cachez le champ de confirmation du mot de passe
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget= forms.PasswordInput, label="Mot de passe")"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=None  # Supprime le texte d'aide
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text=None  # Supprime le texte d'aide
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget= forms.PasswordInput, label="Mot de passe")