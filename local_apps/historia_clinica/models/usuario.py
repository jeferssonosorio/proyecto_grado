import uuid as uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
from local_apps.historia_clinica.managers import UsuarioManager
from local_apps.historia_clinica.models.tipoDocIdentificacion import (
    TipoDocIdentificacion,
)


# Create your models here.
class Usuario(AbstractUser, TimeStampedModel):
    """
    Representa un Usuario en el sistema
    """

    uuid = models.UUIDField(
        db_index=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True)
    tipo_doc_identificacion = models.ForeignKey(
        TipoDocIdentificacion, on_delete=models.CASCADE
    )
    doc_identificacion = models.CharField(max_length=20, unique=True)
    objects = UsuarioManager()

    class Meta:
        app_label = "historia_clinica"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        default_permissions = ()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
