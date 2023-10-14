from django.shortcuts import render
from utilities import import_tools
from recipes.models import RecipeIngredient

def homeView(request):



    return render(request, 'base.html')
