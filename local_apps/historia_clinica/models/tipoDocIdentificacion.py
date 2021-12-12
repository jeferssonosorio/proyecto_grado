from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class TipoDocIdentificacion(TimeStampedModel):
    nombre = models.CharField(max_length=25, unique=True)
    nombreCorto = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.nombre
