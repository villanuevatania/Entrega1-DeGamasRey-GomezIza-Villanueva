from django.db import models
class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    anios_activa = models.IntegerField()
    
    
    def __str__ (self):
        descripcion = f'El nombre del artista es {self.nombre}, pertenece al palo del {self.genero} y está en actividad desde hace {self.anios_activa} años'
        return descripcion
