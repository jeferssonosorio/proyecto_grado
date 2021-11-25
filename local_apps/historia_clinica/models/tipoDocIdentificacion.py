from django.db import models


# Create your models here.
class TipoDocIdentificacion(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    nombreCorto = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.nombre
