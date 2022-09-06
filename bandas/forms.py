from django import forms
from django.db import models
from ckeditor.fields import RichTextFormField

class FormBanda(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    critica = RichTextFormField( required=False)
    fecha_creacion= forms.IntegerField(required=False)
    publicacion = forms.ImageField(required=False)
    fecha_del_post = models.DateField(null=True)

class BusquedaBanda (forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
