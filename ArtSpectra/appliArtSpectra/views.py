from django.shortcuts import render
from appliArtSpectra.models import Oeuvre, Panier, PanierOeuvre
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from appliArtSpectra.forms import OeuvreUpdateForm, OeuvreCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def ajouterOeuvre(request):
    if request.method == 'POST':
        form_oeuvre = OeuvreCreateForm(request.POST, request.FILES)
        if form_oeuvre.is_valid():
            oeuvre = form_oeuvre.save(commit=False)
            oeuvre.auteurOeuvre = request.user  # Assigner l'utilisateur actuel à auteurOeuvre
            oeuvre.save()
            messages.success(request, "Votre oeuvre a bien été ajoutée !")
            return redirect('profil')
    else:
        form_oeuvre = OeuvreCreateForm()
        oeuvres = Oeuvre.objects.filter(auteurOeuvre=request.user)
    return render(request, 'appliArtSpectra/ajouterOeuvre.html', {'form_oeuvre': form_oeuvre, 'oeuvres': oeuvres})



@login_required
def panier(request):
    # Get the current user's cart or create a new one if it doesn't exist
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)

    # Get the artwork in the cart along with their quantities
    panieroeuvres = PanierOeuvre.objects.filter(panier=panier).select_related('oeuvre')

    # Calculate the total price of the items in the cart
    total = sum(panieroeuvre.oeuvre.prixOeuvre * panieroeuvre.quantite for panieroeuvre in panieroeuvres)

    context = {
        'panier': panier,
        'panieroeuvres': panieroeuvres,
        'total': total
    }

    return render(request, 'appliArtSpectra/panier.html', context)


@login_required
def ajouter_au_panier(request, oeuvre_id):
    # Get the selected artwork
    oeuvre = Oeuvre.objects.get(idOeuvre=oeuvre_id)

    # Check if the artwork is available
    if oeuvre.quantiteOeuvre > 0:
        # Get the current user's cart
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)

        # Add the artwork to the cart
        panier_oeuvre, created = PanierOeuvre.objects.get_or_create(panier=panier, oeuvre=oeuvre)
        panier_oeuvre.quantite += 1
        panier_oeuvre.save()

        # Decrease the available quantity of the artwork
        oeuvre.quantiteOeuvre -= 1
        oeuvre.save()

    return redirect('panier')


@login_required
def supprimer_du_panier(request, panieroeuvre_id):
    # Get the PanierOeuvre object to delete
    panieroeuvre = PanierOeuvre.objects.get(id=panieroeuvre_id)

    # Decrease the quantity in the cart by 1
    panieroeuvre.quantite -= 1
    panieroeuvre.save()

    oeuvre = panieroeuvre.oeuvre
    oeuvre.quantiteOeuvre += 1
    oeuvre.save()

    if panieroeuvre.quantite == 0:
        panieroeuvre.delete()

    return redirect('panier')


