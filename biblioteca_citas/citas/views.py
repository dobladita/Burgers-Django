from django.shortcuts import render
from .models import Cita
# Create your views here.

def crear_cita(request):
    if request.method == "POST":
        texto = request.POST.get('texto')
        autor = request.POST.get('autor')
        fecha = request.POST.get('fecha')
        fuente_id = request.POST.get('fuente')
