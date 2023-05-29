from django.shortcuts import render
from accounts.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !!')
            return redirect('oeuvres')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, f'Vous êtes bien déconnecté')
    return redirect('accueil')