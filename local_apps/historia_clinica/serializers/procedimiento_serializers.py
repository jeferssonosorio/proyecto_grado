from rest_framework import serializers
from local_apps.historia_clinica.models.procedimiento import Procedimiento


class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedimiento
        fields = "__all__"
