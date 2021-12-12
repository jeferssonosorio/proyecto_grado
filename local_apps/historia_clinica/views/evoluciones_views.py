from rest_framework import viewsets
from local_apps.historia_clinica.serializers.evoluciones_serializers import (
    EvolucionesSerializer,
)
from local_apps.historia_clinica.models.evoluciones import Evoluciones


class EvolucionesViewSet(viewsets.ModelViewSet):
    queryset = Evoluciones.objects.all()
    serializer_class = EvolucionesSerializer
