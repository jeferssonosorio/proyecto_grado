from django.db import models

# Create your models here.
class Evoluciones(models.Model):
    descripcion = models.TextField()
    fecha = models.DateTimeField()
