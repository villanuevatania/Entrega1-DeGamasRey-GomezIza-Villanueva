from django import forms
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BusquedaBanda, FormBanda
from .models import Banda
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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
  
      return render(request, 'bandas/about.html')

def buscar(request):
  if request.GET["buscar"]:
    var = request.GET["buscar"]
    banda = Banda.objects.filter(nombre__icontains = var)
    return render(request, 'bandas/listado_bandas.html', {'banda': banda})

  else:
    respuesta = 'Debe llenar algun campo.'
    return render(request, 'bandas/listado_bandas.html', {'respuesta': respuesta})


def editar_banda(request):
  return redirect ('listado_bandas') 
    # model=Banda
    # template_name = 'bandas/banda.html'
    # success_url = '/bandas/banda'
    # fields = ['nombre', 'genero', 'anios_activa']

@login_required
def eliminar_banda(request, id):
  banda = Banda.objects.get(id=id)
  banda.delete()
  return redirect('listado_bandas')

