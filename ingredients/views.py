from django.shortcuts import render, redirect
from django.http import HttpResponse
from ingredients.models import Ingredient
from .forms import IngredientForm, NutritionalForm

from django.views.generic.list import ListView
class IngredientListView(ListView):
    template_name = 'ingredients/ingredients.html'
    model = Ingredient
    context_object_name = 'ingredients'

def ingredientDetalilview(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    context = {'object': ingredient}
    return render(request, 'ingredients/ingredient_detail.html', context)


def ingredientCreateView(request):
    form1 = IngredientForm(request.POST or None)
    form2 = NutritionalForm(request.POST or None)

    if form1.is_valid() and form2.is_valid():
        ingredient = form1.save(commit=False)
        nutritionals = form2.save()
        ingredient.nutritional = nutritionals
        ingredient.save()
        print('inside valis')
        return redirect('ingredients/')
    context = {'form1': form1, 'form2': form2, }
    return render(request, 'ingredients/create.html', context)

def checkIngredient(request):
    ingredient=request.POST.get("name")
    if Ingredient.objects.filter(name__iexact=ingredient):
        return HttpResponse('<div id="ingredient-error" class="error">Already exists</div>')
    else:
        return HttpResponse('<div id="ingredient-error" class="success">Available</div>')