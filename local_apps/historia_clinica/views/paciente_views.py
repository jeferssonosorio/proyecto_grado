from rest_framework import viewsets
from local_apps.historia_clinica.serializers.paciente_serializers import (
    PacienteSerializer,
)
from local_apps.historia_clinica.models.paciente import Paciente


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
