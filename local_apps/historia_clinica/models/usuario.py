from django.db import models
from local_apps.historia_clinica.models.tipoDocIdentificacion import (
    TipoDocIdentificacion,
)


# Create your models here.
class Usuario(models.Model):
    # Elcampo usuariohace referencia al Usuario y Contraseña de Logueo
    usuario = models.CharField(max_length=30)
    # contrasenia = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    nombre = models.CharField(max_length=20)
    apellido_1 = models.CharField(max_length=30)
    apellido_2 = models.CharField(max_length=30, blank=True, null=True)
    tipo_doc_identificacion = models.ForeignKey(
        TipoDocIdentificacion, on_delete=models.CASCADE
    )
    doc_identificacion = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return "{} {} {}".format(
            self.nombre,
            self.apellido_1,
            self.apellido_2 if self.apellido_2 is not None else "",
        )
