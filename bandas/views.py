from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Banda

# Create your views here.
def home(request):
    return render(request, 'index.html')
    # return HttpResponse ('<h1> Comunidad DO RE MI fue creado con la finalidad de que puedas cargar una reseña sobre tu/s banda/s, difundir tus shows, conocer nuevas bandas e intercambiar opiniones con otros músicos y/o melómanos.<h1>'
		# '<h1>¡Bienvenido a esta plataforma!<h1>')
    
def un_template(request):
  
  # template = loader.get_template('index.html')
  
  prueba1 = Banda(nombre='Miranda')
  prueba2 = Banda(nombre='Muse')
  prueba3 = Banda(nombre='Deftones')
  
  # render = template.render({})
  
  return render(request, 'mi_template.html', {'lista_bandas': [prueba1, prueba2, prueba3]})

def about(request):
    return HttpResponse ('<h1> Comunidad DO RE MI fue creado con la finalidad de que puedas cargar una reseña sobre tu/s banda/s, difundir tus shows, conocer nuevas bandas e intercambiar opiniones con otros músicos y/o melómanos.<h1>'
		'<h1>¡Bienvenido a esta plataforma!<h1>')