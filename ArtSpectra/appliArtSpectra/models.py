from django.db import models

# Create your models here.
class Oeuvre(models.Model):
    # idOeuvre est la clé primaire, an autoincrement => auto_field
    idOeuvre = models.AutoField(primary_key=True)

    # nomOeuvre est un varchar de 50 caractères => CharField
    nomOeuvre = models.CharField(max_length=50, verbose_name="Nom de l'oeuvre")

    # une methode de type "toString" pour afficher l'objet
    def __str__(self):
        return 'oeuvre ' + self.nomOeuvre