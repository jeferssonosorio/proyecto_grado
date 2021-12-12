from rest_framework import viewsets
from local_apps.historia_clinica.serializers.procedimiento_serializers import (
    ProcedimientoSerializer,
)
from local_apps.historia_clinica.models.procedimiento import Procedimiento


class ProcedimientoViewSet(viewsets.ModelViewSet):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer
