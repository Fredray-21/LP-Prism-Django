from django.db import models


# Create your models here.
class Ingredient(models.Model):
    # idIngredient est la clé primaire, an autoincrement => auto_field
    idIngredient = models.AutoField(primary_key=True)

    # nomIngredient est un varchar de 50 caractères => CharField
    nomIngredient = models.CharField(max_length=50, verbose_name="Nom de l'ingrédient")

    # une methode de type  "toString" pour afficher l'objet
    def __str__(self):
        return 'ingredient ' + self.nomIngredient


class Pizza(models.Model):
    # idPizza est la clé primaire, an autoincrement => auto_field
    idPizza = models.AutoField(primary_key=True)

    # nomPizza est un varchar de 50 caractères => CharField
    nomPizza = models.CharField(max_length=50, verbose_name="Nom de la pizza")

    # prixPizza est un float => DecimalField
    prixPizza = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Prix de la pizza")

    # une methode de type  "toString" pour afficher l'objet
    def __str__(self):
        return 'pizza ' + self.nomPizza + ' (prix = ' + str(self.prixPizza) + '€)'


class Composition(models.Model):
    # la classe Meta qui gère l'unicité du couple des clés étrangères
    class Meta:
        unique_together = (('ingredient', 'pizza'))

    # idComposition est la clé primaire, an autoincrement => auto_field
    idComposition = models.AutoField(primary_key=True)

    # les deux clés étrangères, dont les noms sont les noms des classes associées
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    # l'autre champ, chainage de caractères
    quantite = models.CharField(max_length=100, verbose_name="Quantité de l'ingrédient")

    # méthode d'affichage
    def __str__(self):
        ing = self.ingredient
        piz = self.pizza
        return ing.__str__() + ' fait partie de la pizza ' + piz.__str__() + ' (quantité = ' + self.quantite + ')'


