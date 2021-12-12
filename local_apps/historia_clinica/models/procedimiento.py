from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Procedimiento(TimeStampedModel):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
