from django.db import models

class Posteo (models.Model):
    contenido = models.CharField(max_length=300)
    autor = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True)
    image = models.ImageField(upload_to='imagepost', null=True, blank=True)
    
    def __str__(self):
        return (f'Este posteo pertenece a {self.autor}')
