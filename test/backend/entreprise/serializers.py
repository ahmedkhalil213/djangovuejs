from rest_framework import serializers
from .models import Entreprise

class EntrepriseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'

    def validate_siret(self, value):
        # Add validation logic for SIRET format
        if not value.isdigit() or len(value) != 14:
            raise serializers.ValidationError("Invalid SIRET format. SIRET must be 14 digits long.")
        return value
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'
class SiretSerializer(serializers.Serializer):
    siret = serializers.CharField(max_length=14)

class EntrepriseIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ['id']