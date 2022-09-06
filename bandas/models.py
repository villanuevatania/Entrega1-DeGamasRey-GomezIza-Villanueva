from django.db import models
from ckeditor.fields import RichTextField

class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    critica= RichTextField()
    fecha_creacion= models.IntegerField(null=True, blank=True)
    publicacion = models.ImageField(upload_to= 'posteos', null = True, blank = True)
    fecha_del_post = models.DateField(null=True)
    
def __str__ (self):
        return f'El nombre del artista es {self.nombre}, pertenece al palo del {self.genero} y está en actividad desde hace {self.fecha_de_formacion} años'