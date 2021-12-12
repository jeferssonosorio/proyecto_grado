import datetime
from django.db import models
from django_extensions.db.models import TimeStampedModel
from local_apps.historia_clinica.models.afecciones import Afecciones
from local_apps.historia_clinica.models.paciente import Paciente


class Diagnostico(TimeStampedModel):
    afecciones = models.ManyToManyField(Afecciones)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Paciente: {} | Fecha: {}".format(self.paciente.documento, self.fecha)
