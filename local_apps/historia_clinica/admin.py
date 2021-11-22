from django.contrib import admin
from local_apps.historia_clinica.models.evoluciones import Evoluciones
from local_apps.historia_clinica.models.paciente import Paciente

# Register your models here.
admin.site.register(Evoluciones)
admin.site.register(Paciente)
