from django.db import models
from django_extensions.db.models import TimeStampedModel

CÉDULA_CIUDADANÍA = "CC"
TARJETA_IDENTIDAD = "TI"
PASAPORTE = "PA"
CARNET_DIPLOMÁTICO = "CD"

TIPOS_DOCUMENTOS_IDENTIFICACION = (
    (CÉDULA_CIUDADANÍA, "CÉDULA CIUDADANÍA"),
    (TARJETA_IDENTIDAD, "TARJETA IDENTIDAD"),
    (PASAPORTE, "PASAPORTE"),
    (CARNET_DIPLOMÁTICO, "CARNET DIPLOMÁTICO"),
)
# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_1 = models.CharField(max_length=30)
    apellido_2 = models.CharField(max_length=30, blank=True, null=True)
    tipo_documento_identificacion = models.CharField(
        choices=TIPOS_DOCUMENTOS_IDENTIFICACION, max_length=2
    )
    documento = models.CharField(max_length=20, unique=True, null=True)

    class Meta:
        abstract = True
