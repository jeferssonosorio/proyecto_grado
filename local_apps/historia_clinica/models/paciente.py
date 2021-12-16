from django.db import models
from django_extensions.db.models import TimeStampedModel
from local_apps.historia_clinica.models.patologia import Patologia
from local_apps.historia_clinica.models.persona import Persona


# Create your models here.
class Paciente(Persona, TimeStampedModel):

    O_NEGATIVO = "O-"
    O_POSITIVO = "O+"
    A_NEGATIVO = "A-"
    A_POSITIVO = "A+"
    B_NEGATIVO = "B-"
    B_POSITIVO = "B+"
    AB_NEGATIVO = "AB-"
    AB_POSITIVO = "AB+"

    GRUPOS_SANGUINEOS = [
        (O_NEGATIVO, "O-"),
        (O_POSITIVO, "O+"),
        (A_NEGATIVO, "A-"),
        (A_POSITIVO, "A+"),
        (B_NEGATIVO, "B-"),
        (B_POSITIVO, "B+"),
        (AB_NEGATIVO, "AB-"),
        (AB_POSITIVO, "AB+"),
    ]
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=20, blank=True, null=True)
    grupo_sanguineo = models.CharField(choices=GRUPOS_SANGUINEOS, max_length=3)
    # Definida en metros
    estatura = models.DecimalField(max_digits=3, decimal_places=2)

    # Definida en Kilogramos
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    patologia = models.ManyToManyField(Patologia, blank=True)

    def __str__(self):
        return "{} {} {}".format(
            self.nombre,
            self.apellido_1,
            self.apellido_2 if self.apellido_2 is not None else "",
        )
