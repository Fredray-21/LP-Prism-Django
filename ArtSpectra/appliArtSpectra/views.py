from django.shortcuts import render
from appliArtSpectra.models import Oeuvre
# Create your views here.

def accueil(request):
    return render(request, 'appliArtSpectra/accueil.html')

def oeuvres(request):
    oeuvres = Oeuvre.objects.all()
    return render(request, 'appliArtSpectra/oeuvres.html', {'oeuvres': oeuvres})