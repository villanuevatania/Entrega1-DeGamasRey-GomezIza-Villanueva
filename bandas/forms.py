from django import forms
from django.db import models
class FormBanda(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    fecha_de_formacion = forms.IntegerField(required=False)
    critica = forms.CharField(max_length=100, required=False)
    imagen = forms.ImageField(required=False)
    fecha_del_post = models.DateField(null=True)

class BusquedaBanda (forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
