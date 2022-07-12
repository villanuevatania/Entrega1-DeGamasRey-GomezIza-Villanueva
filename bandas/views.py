from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .forms import BusquedaBanda, FormBanda
from .models import Banda

# Create your views here.
def home(request):
  return render(request, 'index.html')
    
def crear_banda(request):
  

  if request.method == 'POST':
    form = FormBanda(request.POST)
    
    if form.is_valid():
      data = form.cleaned_data
      
      banda = Banda(
        nombre=data.get('nombre'),
        genero=data.get('genero'),
        anios_activa=data.get('anios_activa')
      )
      banda.save()
      
      listado_bandas = Banda.objects.all()
      
      return render(request, 'listado_bandas.html', {'listado_bandas': listado_bandas})
    
    else:
      return render(request, 'crear_banda.html', {'form': form})
  
  form_banda = FormBanda()
  
  
  return render(request, 'crear_banda.html', {'form': form_banda})

def listado_bandas(request):
  
  nombre_de_busqueda = request.GET.get('banda')
  
  if nombre_de_busqueda:
    listado_bandas = Banda.objects.filter(banda__icontains = nombre_de_busqueda)
  else:
    listado_bandas = Banda.objects.all()
    form = BusquedaBanda()
  
  return render(request, 'listado_bandas.html', {'listado_bandas': listado_bandas, 'form':form})


def about(request):
    return HttpResponse ('<h1> Comunidad DO RE MI fue creado con la finalidad de que puedas cargar una reseña sobre tu/s banda/s, difundir tus shows, conocer nuevas bandas e intercambiar opiniones con otros músicos y/o melómanos.<h1>'
		'<h1>¡Bienvenido a esta plataforma!<h1>')
    
def buscar(request):

    var2 = Banda.objects.all()
    contexto = { "todos" : var2 }

    if request.GET:

        var = request.GET["buscar"]

        buscador = Banda.objects.filter(nombre__icontains = var)

        contexto = { "buscados" : buscador , "todos" : var2 }

        plantilla = loader.get_template("buscador.html")
        documento = plantilla.render( contexto )
        
        return HttpResponse( documento )
    
    plantilla = loader.get_template("buscador.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )