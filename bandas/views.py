from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Banda

# Create your views here.
def home(request):
  return render(request, 'index.html')
    
def crear_banda(request):
  
  # print(request.GET)
  
  nombre = request.POST.get('nombre')
  genero = request.POST.get('genero')
  anios_activa = request.POST.get('anios_activa')
  
  banda = Banda(nombre=nombre, genero=genero, anios_activa=anios_activa)
  banda.save()
  
  
  return render(request, 'crear_banda.html', {'banda': banda})

def about(request):
    return HttpResponse ('<h1> Comunidad DO RE MI fue creado con la finalidad de que puedas cargar una reseña sobre tu/s banda/s, difundir tus shows, conocer nuevas bandas e intercambiar opiniones con otros músicos y/o melómanos.<h1>'
		'<h1>¡Bienvenido a esta plataforma!<h1>')