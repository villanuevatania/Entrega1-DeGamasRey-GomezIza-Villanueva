from django.db import models
from ckeditor.fields import RichTextField
class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    fecha_de_formacion = models.IntegerField()
    critica= RichTextField(null = True)
    fecha_del_post = models.DateField(null=True)    
    
def __str__ (self):
        return f'El nombre del artista es {self.nombre}, pertenece al palo del {self.genero} y está en actividad desde hace {self.fecha_de_formacion} años'

class MasDatosPosteo(models.Model):
    banda = models.OneToOneField(Banda, on_delete=models.CASCADE)
    publicacion = models.ImageField(upload_to= 'posteos', null = True, blank = True)