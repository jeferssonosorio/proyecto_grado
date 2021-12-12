import datetime
from django.db import models
from django_extensions.db.models import TimeStampedModel
from local_apps.historia_clinica.models.procedimiento import Procedimiento
from local_apps.historia_clinica.models.usuario import Usuario
from local_apps.historia_clinica.models.diagnostico import Diagnostico

# Create your models here.
class Evoluciones(TimeStampedModel):
    descripcion = models.TextField()
    fecha = models.DateField(default=datetime.date.today)
    procedimiento = models.ManyToManyField(Procedimiento)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)

    def __str__(self):
        procedimiento = ", ".join(
            str(procedimiento) for procedimiento in self.procedimiento.all()
        )
        return "Paciente: {} | Fecha Diagnostico: {} | Procedimientos: {}".format(
            self.diagnostico.paciente.documento,
            self.diagnostico.fecha,
            procedimiento,
        )
