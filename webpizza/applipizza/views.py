from django.shortcuts import render
from applipizza.models import Pizza

# Create your views here.
def pizzas(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})


