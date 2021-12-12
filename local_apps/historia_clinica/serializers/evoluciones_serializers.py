from rest_framework import serializers
from local_apps.historia_clinica.models.evoluciones import Evoluciones


class EvolucionesSerializer(serializers.ModelSerializer):
    fecha = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = Evoluciones
        fields = "__all__"
