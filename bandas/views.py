from django import forms
import datetime
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BusquedaBanda, FormBanda
from .models import Banda, Imagen
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
  return render(request, 'index.html')
    
    
def crear_banda(request):
  
  if request.method == 'POST':
    form = FormBanda(request.POST, request.FILES)
    
    if form.is_valid():
      data = form.cleaned_data
      banda = Banda(
        nombre=data.get('nombre'),
        genero=data.get('genero'),
        fecha_de_formacion=data.get('fecha_de_formacion'),
        critica=data.get('critica'),
        fecha_del_post = datetime.datetime.now(),
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
    
    form = BusquedaBanda()
    return render(request, 'bandas/listado_bandas.html', {'listado_bandas': listado_bandas, 'form':form})


class ListadoBandas(ListView):
    model=Banda
    template_name = 'bandas/listado_bandas.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaBanda()
        return context


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


@login_required
def editar_banda(request, id):
  banda = Banda.objects.get(id=id)

  
  if request.method == 'POST':
    form = FormBanda(request.POST, request.FILES)    
    if form.is_valid():      
      banda.nombre = form.cleaned_data.get('nombre')
      banda.genero = form.cleaned_data.get('genero')
      banda.fecha_de_formacion = form.cleaned_data.get('fecha_de_formacion')
      banda.critica= form.cleaned_data.get('critica')
      banda.save()
      
      return redirect('listado_bandas')
    
    else:
      return render (request, 'bandas/editar_banda.html',{'form':form,'banda':banda})
      
  form_banda = FormBanda(initial = {'nombre': banda.nombre,'genero': banda.genero,'fecha_de_formacion': banda.fecha_de_formacion,'critica': banda.critica})
  
  
  return render(request, 'bandas/editar_banda.html', {'form': form_banda,'banda':banda})


@login_required
def eliminar_banda(request, id):
  banda = Banda.objects.get(id=id)
  banda.delete()
  return redirect('listado_bandas')


def mostrar_banda(request, id):
  banda = Banda.objects.get(id=id)
  
  return render(request, 'bandas/mostrar_banda.html',{'banda':banda})


def home_view(request):
    return render_to_response('base.html')

