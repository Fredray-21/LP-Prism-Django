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


