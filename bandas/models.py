from django.db import models

class Banda(models.Model):
    nombre = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    anios_activa = models.IntegerField()
    
    
    def __str__ (self):
        return f'El nombre del artista es {self.nombre}, pertenece al palo del {self.genero} y está en actividad desde {self.anios_activa}'