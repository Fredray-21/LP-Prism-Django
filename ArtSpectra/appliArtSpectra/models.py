from django.db import models
from accounts.models import Shopper

# Create your models here.
class Oeuvre(models.Model):
    # idOeuvre est la clé primaire, an autoincrement => auto_field
    idOeuvre = models.AutoField(primary_key=True)

    # nomOeuvre est un varchar de 50 caractères => CharField
    nomOeuvre = models.CharField(max_length=50, verbose_name="Nom de l'oeuvre", unique=True)

    # descriptionOeuvre est un varchar de 255 caractères => CharField
    descriptionOeuvre = models.CharField(max_length=255, verbose_name="Description de l'oeuvre", blank=True,default='')

    # dateCreationOeuvre est un date => DateField
    dateCreationOeuvre = models.CharField(max_length=10,verbose_name="Date de création de l'oeuvre")

    # dimensionOeuvre est un varchar de 50 caractères => CharField
    dimensionOeuvre = models.CharField(max_length=50, verbose_name="Dimension de l'oeuvre", blank=True)

    imageOeuvre = models.ImageField(upload_to='images/oeuvres/', verbose_name="Image de l'oeuvre", blank=True)

    prixOeuvre = models.IntegerField(verbose_name="Prix de l'oeuvre")

    slug = models.SlugField(max_length=100, verbose_name="Slug de l'oeuvre", unique=False, editable=True)

    # auteurOeuvre est une clé étrangère vers le modèle Shopper
    auteurOeuvre = models.ForeignKey(Shopper, on_delete=models.CASCADE, verbose_name="Auteur de l'oeuvre")

    quantiteOeuvre = models.IntegerField(verbose_name="Quantité de l'oeuvre")

    # une methode de type "toString" pour afficher l'objet
    def __str__(self):
        return 'oeuvre ' + self.nomOeuvre



class Panier(models.Model):
    utilisateur = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    oeuvre = models.ManyToManyField(Oeuvre, through='PanierOeuvre')

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"


class PanierOeuvre(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    oeuvre = models.ForeignKey(Oeuvre, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)
    # Additional fields specific to the relationship between Panier and Oeuvre

    class Meta:
        db_table = 'panier_oeuvre'  # Optional: Define a custom database table name