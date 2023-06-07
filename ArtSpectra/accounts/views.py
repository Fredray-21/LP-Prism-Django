from django.shortcuts import render
from accounts.forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import Shopper
from appliArtSpectra.models import Oeuvre
from django.db.models import Count

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
    return render(request, 'accounts/signup-login.html', {'form_signup': form_signup})


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
    return render(request, 'accounts/signup-login.html', {'form_login': form_login})


def profil(request):
    if request.method == 'POST':
        form_profil = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form_profil.is_valid():
            form_profil.save()
            messages.success(request, f'Votre profil a été mis à jour avec succès')
            return redirect('profil')
    else:
        form_profil = UserUpdateForm(instance=request.user)
        oeuvres = Oeuvre.objects.filter(auteurOeuvre=request.user)
    return render(request, 'accounts/profil.html', {'form_profil': form_profil, 'oeuvres': oeuvres})


def artiste(request, username):
    try :
        artiste = Shopper.objects.get(username=username)
        oeuvreDeArtiste = Oeuvre.objects.filter(auteurOeuvre=artiste)
    except :
        messages.error(request, f'Ce profil n\'existe pas')
        return redirect('accueil')

    return render(request, 'accounts/artiste.html', {'artiste': artiste, 'oeuvreDeArtiste': oeuvreDeArtiste})

def artistes(request):
    artistes = Shopper.objects.annotate(nb_oeuvres=Count('oeuvre')).filter(nb_oeuvres__gt=0)
    dictArtiste = []
    for artiste in artistes:
        dictArtiste.append({
            'artiste_obj': artiste,
            'nb_oeuvres': Oeuvre.objects.filter(auteurOeuvre=artiste).count(),
            'first_oeuvre': Oeuvre.objects.filter(auteurOeuvre=artiste).last(),
        }),
    print(dictArtiste)


    return render(request, 'accounts/artistes.html', {'artistes': dictArtiste})