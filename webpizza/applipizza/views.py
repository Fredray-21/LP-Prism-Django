from django.shortcuts import render
from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition
from applipizza.forms import IngredientForm
from applipizza.forms import PizzaForm

# Create your views here.
def pizzas(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})


def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'applipizza/ingredients.html', {'ingredients': lesIngredients})


def pizza(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza=pizza_id)
    laComposition = Composition.objects.filter(pizza_id=pizza_id)
    lesIngredients = []
    for c in laComposition:
        lesIngredients.append([Ingredient.objects.get(idIngredient=c.ingredient_id), c.quantite])
    return render(request, 'applipizza/pizza.html', {'pizza': laPizza, 'ingredients': lesIngredients})


def formulaireCreationIngredient(request):
    formulaire = IngredientForm()
    return render(request, "applipizza/formulaireCreationIngredient.html", {"form": formulaire})


def creerIngredient(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            nomIng = form.cleaned_data['nomIngredient']
            ingredient = Ingredient()
            ingredient.nomIngredient = nomIng
            ingredient.save()
            return render(request, "applipizza/traitementFormulaireCreationIngredient.html", {"ingredient": ingredient})
    else:
        form = IngredientForm()
    return render(request, "applipizza/formulaireCreationIngredient.html", {"form": form})

def formulaireCreationPizza(request):
    formulaire = PizzaForm()
    return render(request, "applipizza/formulaireCreationPizza.html", {"form": formulaire})

def creerPizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            nomPizza = form.cleaned_data['nomPizza']
            prixPizza = form.cleaned_data['prixPizza']
            pizza = Pizza()
            pizza.nomPizza = nomPizza
            pizza.prixPizza = prixPizza
            pizza.save()
            return render(request, "applipizza/traitementFormulaireCreationPizza.html", {"pizza": pizza})
    else:
        form = PizzaForm()
    return render(request, "applipizza/formulaireCreationPizza.html", {"form": form})