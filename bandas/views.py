from datetime import datetime
from django.shortcuts import redirect, render
from .forms import BusquedaBanda, FormBanda
from .models import Banda
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
  return render(request, 'index.html')

def about(request):
  
  return render(request, 'bandas/about.html')

def listado_bandas(request):
    busqueda = request.GET.get('nombre')
    
    if busqueda:
      listado_bandas = Banda.objects.filter(nombre__icontains=busqueda)
    else:
      listado_bandas = Banda.objects.all()
      
    form = BusquedaBanda()
    return render(request, 'bandas/listado_bandas.html', {'listado_bandas': listado_bandas, 'form':form})

def crear_banda(request):
  
  if request.method == 'POST':
    form = FormBanda(request.POST, request.FILES)
    
    
    if form.is_valid():
      data = form.cleaned_data
      fecha_del_post= data.get('fecha_del_post')
      if not fecha_del_post:
        fecha_del_post = datetime.now()
        
      banda = Banda(
        nombre=data.get('nombre'),
        genero=data.get('genero'),
        critica=data.get('critica'),
        fecha_creacion=data.get('fecha_creacion'),
        publicacion=data.get('publicacion'),
        fecha_del_post = fecha_del_post
      )
      banda.save()
      
      return redirect('listado_bandas')
    
    else:
      return render(request, 'bandas/crear_banda.html', {'form': form})
  form_banda = FormBanda()
  
  return render(request, 'bandas/crear_banda.html', {'form': form_banda})


@login_required
def editar_banda(request, id):
  banda = Banda.objects.get(id=id)
  
  if request.method == 'POST':
    form = FormBanda(request.POST, request.FILES)    
    if form.is_valid():      
      banda.nombre = form.cleaned_data.get('nombre')
      banda.genero = form.cleaned_data.get('genero')
      banda.fecha_creacion = form.cleaned_data.get('fecha_creacion')
      banda.critica= form.cleaned_data.get('critica')
      banda.publicacion = form.cleaned_data.get('publicacion')
      banda.save()
      
      return redirect('listado_bandas')
    
    else:
      return render (request, 'bandas/editar_banda.html',{'form':form,'banda':banda})
      
  form_banda = FormBanda(
    initial = {
      'nombre': banda.nombre,
      'genero': banda.genero,
      'fecha_creacion': banda.fecha_creacion,
      'critica': banda.critica,
      'publicacion': banda.publicacion,
      }
    )
  
  return render(request, 'bandas/editar_banda.html', {'form': form_banda,'banda':banda})


@login_required
def eliminar_banda(request, id):
  banda = Banda.objects.get(id=id)
  banda.delete()
  return redirect('listado_bandas')


def mostrar_banda(request, id):
  banda = Banda.objects.get(id=id)
  return render(request, 'bandas/mostrar_banda.html',{'banda':banda})