import datetime
from django.db import models
from local_apps.historia_clinica.models.paciente import Paciente
from local_apps.historia_clinica.models.procedimiento import Procedimiento
from local_apps.historia_clinica.models.usuario import Usuario


# Create your models here.
class Evoluciones(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField(default=datetime.date.today)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    procedimiento = models.ManyToManyField(Procedimiento)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "Paciente: {}, Fecha: {}".format(self.paciente, self.fecha)
