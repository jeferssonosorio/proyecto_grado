from django.contrib import admin
from local_apps.historia_clinica.models.paciente import Paciente
from local_apps.historia_clinica.models.patologia import Patologia


# Register your models here.
admin.site.register([Paciente, Patologia])
