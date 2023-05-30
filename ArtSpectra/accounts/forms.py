from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Shopper

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = Shopper
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    class Meta:
        model = Shopper
        fields = ('username', 'password')



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    avatar = forms.ImageField(label='Avatar', required=False)
    presentation = forms.CharField(label='Présentation', widget=forms.Textarea, required=False)

    class Meta:
        model = Shopper
        fields = ('first_name', 'last_name', 'email', 'avatar', 'presentation')