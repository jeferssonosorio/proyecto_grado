from rest_framework import serializers
from local_apps.historia_clinica.models.paciente import Paciente


class PacienteSerializer(serializers.Serializer):
    class Meta:
        model = Paciente
        fields = "__all__"
