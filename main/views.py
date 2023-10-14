from django.shortcuts import render
from utilities import import_tools
from recipes.models import RecipeIngredient
from utilities.import_tools import fixVerduraFresca


def homeView(request):


    return render(request, 'base.html')
