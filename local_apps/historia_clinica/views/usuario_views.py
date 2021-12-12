from rest_framework import viewsets
from local_apps.historia_clinica.serializers.usuario_serializers import (
    UsuarioSerializer,
)
from local_apps.historia_clinica.models.usuario import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
