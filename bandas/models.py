from django.db import models
from distutils.command.upload import upload
from django import forms

class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    fecha_de_formacion = models.IntegerField()
    critica= models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'posteos', null = True)
    fecha_del_post = models.DateField(null=True)
    
    
def __str__ (self):
        return f'El nombre del artista es {self.nombre}, pertenece al palo del {self.genero} y está en actividad desde hace {self.fecha_de_formacion} años'


class Imagen(models.Model):
    ...