from django.shortcuts import render
from applipizza.models import Pizza
from applipizza.models import Ingredient

# Create your views here.
def pizzas(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'applipizza/ingredients.html', {'ingredients':lesIngredients})