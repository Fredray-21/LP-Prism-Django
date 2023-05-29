from django.shortcuts import render
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form_signup = UserRegistrationForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            username = form_signup.cleaned_data.get('username')
            password = form_signup.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !!')
            return redirect('oeuvres')
    else:
        form_signup = UserRegistrationForm()
        form_login = UserLoginForm()
    return render(request, 'accounts/signup-login.html', {'form_signup': form_signup, 'form_login': form_login})


def logout_user(request):
    logout(request)
    messages.success(request, f'Vous êtes bien déconnecté')
    return redirect('accueil')


def login_user(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password = form_login.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Vous êtes bien connecté')
                return redirect('accueil')
            else:
                messages.error(request, f'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form_login = UserLoginForm()
        form_signup = UserRegistrationForm()
    return render(request, 'accounts/signup-login.html', {'form_signup': form_signup, 'form_login': form_login})