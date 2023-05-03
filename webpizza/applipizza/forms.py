from django import forms
from django.forms import ModelForm
from applipizza.models import Ingredient,Pizza

class IngredientForm(ModelForm) :
    class Meta :
        model = Ingredient
        fields = ['nomIngredient']


class PizzaForm(ModelForm) :
    class Meta :
        model = Pizza
        fields = ['nomPizza', 'prixPizza']
