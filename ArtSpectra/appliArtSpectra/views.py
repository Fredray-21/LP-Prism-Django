from django.shortcuts import render
from appliArtSpectra.models import Oeuvre
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from appliArtSpectra.forms import OeuvreUpdateForm
from django.contrib import messages

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



def supprimerOeuvre(request, idOeuvre):
    oeuvre = get_object_or_404(Oeuvre, idOeuvre=idOeuvre)
    oeuvre.delete()
    return redirect('profil')


def modifierOeuvre(request, idOeuvre):
    oeuvre = get_object_or_404(Oeuvre, idOeuvre=idOeuvre)
    if request.method == 'POST':
        form_oeuvre = OeuvreUpdateForm(request.POST, request.FILES, instance=oeuvre)
        if form_oeuvre.is_valid():
            form_oeuvre.save()
            messages.success(request, f'Votre oeuvre a bien été modifiée !')
            return redirect('profil')
    else:
        form_oeuvre = OeuvreUpdateForm(instance=oeuvre)
        oeuvres = Oeuvre.objects.filter(auteurOeuvre=request.user)
    return render(request, 'appliArtSpectra/modifierOeuvre.html', {'form_oeuvre': form_oeuvre, 'oeuvres': oeuvres})

