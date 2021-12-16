from rest_framework import viewsets
from local_apps.historia_clinica.serializers.patologia_serializers import (
    PatologiaSerializer,
)
from local_apps.historia_clinica.models.patologia import Patologia


class PatologiaViewSet(viewsets.ModelViewSet):
    queryset = Patologia.objects.all()
    serializer_class = PatologiaSerializer
