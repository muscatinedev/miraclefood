from django.shortcuts import render
from utilities import import_tools
def homeView(request):



    return render(request, 'base.html')
