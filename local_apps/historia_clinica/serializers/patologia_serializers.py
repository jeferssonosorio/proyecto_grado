from rest_framework import serializers
from local_apps.historia_clinica.models.patologia import Patologia


class PatologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patologia
        fields = "__all__"
