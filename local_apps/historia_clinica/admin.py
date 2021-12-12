from django.contrib import admin
from local_apps.historia_clinica.models.afecciones import Afecciones
from local_apps.historia_clinica.models.diagnostico import Diagnostico
from local_apps.historia_clinica.models.evoluciones import Evoluciones
from local_apps.historia_clinica.models.paciente import Paciente
from local_apps.historia_clinica.models.procedimiento import Procedimiento
from local_apps.historia_clinica.models.patologia import Patologia
from local_apps.historia_clinica.models.usuario import Usuario
from local_apps.historia_clinica.models.tipoDocIdentificacion import (
    TipoDocIdentificacion,
)

# Register your models here.
admin.site.register(
    [
        Evoluciones,
        Paciente,
        Patologia,
        Procedimiento,
        TipoDocIdentificacion,
        Usuario,
        Afecciones,
        Diagnostico,
    ]
)
