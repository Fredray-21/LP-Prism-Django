from django.shortcuts import render
from appliArtSpectra.models import Oeuvre
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def accueil(request):
    return render(request, 'appliArtSpectra/accueil.html')

def oeuvres(request):
    oeuvres = Oeuvre.objects.all()
    return render(request, 'appliArtSpectra/oeuvres.html', {'oeuvres': oeuvres})

def oeuvre(request, slug, idOeuvre):
    try:
        oeuvre = get_object_or_404(Oeuvre, idOeuvre=idOeuvre)
        # 4 premières oeuvres de l'auteur de l'oeuvre en cours sans l'oeuvre en cours
        oeuvresAuteur = Oeuvre.objects.filter(auteurOeuvre=oeuvre.auteurOeuvre).exclude(idOeuvre=oeuvre.idOeuvre)[:4]
        if oeuvre.slug != slug:
            return redirect('oeuvre', slug=oeuvre.slug, idOeuvre=oeuvre.idOeuvre)
        else :
            return render(request, 'appliArtSpectra/oeuvre.html', {'oeuvre': oeuvre, 'oeuvresAuteur': oeuvresAuteur})
    except: Oeuvre.DoesNotExist
    return redirect('oeuvres')

def typeOeuvre(request, slug):
    slugTypeOeuvre = slug.split("/")[-1]
    typeOeuvre = []
    for oeuvre in Oeuvre.objects.all():
        if oeuvre.slug not in typeOeuvre:
            typeOeuvre.append(oeuvre.slug)

    print("typeOeuvre",typeOeuvre)
    if slugTypeOeuvre in typeOeuvre:
        oeuvres = Oeuvre.objects.filter(slug=slugTypeOeuvre)
        return render(request, 'appliArtSpectra/oeuvres.html', {'oeuvres': oeuvres})
    else:
        return redirect('oeuvres')

def profil(request):
    return render(request, 'appliArtSpectra/profil.html')