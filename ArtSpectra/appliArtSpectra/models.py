from django.db import models

# Create your models here.
class Oeuvre(models.Model):
    # idOeuvre est la clé primaire, an autoincrement => auto_field
    idOeuvre = models.AutoField(primary_key=True)

    # nomOeuvre est un varchar de 50 caractères => CharField
    nomOeuvre = models.CharField(max_length=50, verbose_name="Nom de l'oeuvre", unique=True, default='')

    # descriptionOeuvre est un varchar de 255 caractères => CharField
    descriptionOeuvre = models.CharField(max_length=255, verbose_name="Description de l'oeuvre", blank=True,default='')

    # dateCreationOeuvre est un date => DateField
    dateCreationOeuvre = models.DateField(verbose_name="Date de création de l'oeuvre", default='1900-01-01')

    # dimensionOeuvre est un varchar de 50 caractères => CharField
    dimensionOeuvre = models.CharField(max_length=50, verbose_name="Dimension de l'oeuvre", blank=True,default='')

    # une methode de type "toString" pour afficher l'objet
    def __str__(self):
        return 'oeuvre ' + self.nomOeuvre