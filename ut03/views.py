from django.shortcuts import render
from .forms import CreaTableroForm

# Create your views here.
def welcome(request):
    return render(request, 'ut03/index.html', {})

def crea_tablero(request):
    tablero_form = CreaTableroForm()
    return render(request, 'ut03/crea_tablero.html', {'form':tablero_form})