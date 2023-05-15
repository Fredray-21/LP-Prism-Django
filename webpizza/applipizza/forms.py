from django import forms
from django.forms import ModelForm
from applipizza.models import Ingredient, Pizza, Composition


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['nomPizza', 'prixPizza']



class CompositionForm(ModelForm):
    def __init__(self, idPizza, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pizza = Pizza.objects.get(idPizza=idPizza)
        used_ingredients = Composition.objects.filter(pizza=pizza).values_list('ingredient', flat=True)
        self.fields['ingredient'].label_from_instance = lambda obj: obj.nomIngredient.capitalize()
        # self.fields['ingredient'].queryset = Ingredient.objects.exclude(idIngredient__in=used_ingredients)

    class Meta:
        model = Composition
        fields = ['ingredient', 'quantite']
