from rest_framework import serializers
from local_apps.historia_clinica.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
