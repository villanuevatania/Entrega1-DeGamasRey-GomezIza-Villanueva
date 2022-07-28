from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BusquedaBanda, FormBanda
from .models import Banda
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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
      
      return render(request, 'bandas/listado_bandas.html', {'listado_bandas': listado_bandas})
    
    else:
      return render(request, 'bandas/crear_banda.html', {'form': form})
  
  form_banda = FormBanda()
  
  
  return render(request, 'bandas/crear_banda.html', {'form': form_banda})

def listado_bandas(request):
    listado_bandas = Banda.objects.all()
  
  # nombre_de_busqueda = request.GET.get('buscador')
  
  # if nombre_de_busqueda:
  #   listado_bandas = Banda.objects.filter(banda__icontains = nombre_de_busqueda)
  # else:
    
  
    form = BusquedaBanda()
    return render(request, 'bandas/listado_bandas.html', {'listado_bandas': listado_bandas, 'form':form})


def about(request):
    return HttpResponse ('<h1> Comunidad DO RE MI fue creado con la finalidad de que puedas cargar una reseña sobre tu/s banda/s, difundir tus shows, conocer nuevas bandas e intercambiar opiniones con otros músicos y/o melómanos.<h1>'
		'<h1>¡Bienvenido a esta plataforma!<h1>')
    
def buscar(request):
  if request.GET["buscar"]:
    var = request.GET["buscar"]
    banda = Banda.objects.filter(nombre__icontains = var)
    return render(request, 'bandas/listado_bandas.html', {'banda': banda})
    # if banda.exists():
    # else:
    #   respuesta = 'No existen datos cargados con esa letra.'
    # return render(request, 'listado_bandas.html', {'respuesta': respuesta})
  else:
    respuesta = 'Debe llenar algun campo.'
    return render(request, 'bandas/listado_bandas.html', {'respuesta': respuesta})
    
def editar_bandas (LoginRequiredMixin, UpdateView):
    model=Banda
    template_name = 'bandas/banda.html'
    success_url = '/bandas/banda'
    fields = ['nombre', 'genero', 'anios_activa']


def eliminar_bandas(LoginRequiredMixin, DeleteView):
  banda = Banda.objects.get(id=id)
  banda.delete()
  return redirect('listado_bandas')

def mostrar_bandas(request, id):
  banda = Banda.objects.get(id=id)
  return render(request, 'bandas/mostrar_bandas.html', {'banda': banda})