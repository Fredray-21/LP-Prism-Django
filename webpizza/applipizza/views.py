from django.shortcuts import render
from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition
from applipizza.forms import IngredientForm

# Create your views here.
def pizzas(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'applipizza/ingredients.html', {'ingredients':lesIngredients})

def pizza(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    laComposition = Composition.objects.filter(pizza_id = pizza_id)
    lesIngredients = []
    for c in laComposition:
        lesIngredients.append([Ingredient.objects.get(idIngredient = c.ingredient_id),c.quantite])
    return render(request, 'applipizza/pizza.html', {'pizza': laPizza,'ingredients':lesIngredients})


def formulaireCreationIngredient(request) :
    formulaire = IngredientForm()
    return render(request, "applipizza/formulaireCreationIngredient.html",{"form":formulaire})
