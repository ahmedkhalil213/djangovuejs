from rest_framework import serializers
from .models import Compteur
class CompteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compteur
        fields = ['pdl', 'entre','entreprise']

    def validate_pdl(self, value):
        if len(value) != 14:
            raise serializers.ValidationError("Invalid PDL length. Must be 14 characters long.")
        return value

    def validate(self, data):
        if data['entre'] == 'GAZ' and (not data['pdl'].startswith('GI') or len(data['pdl']) != 6):
            raise serializers.ValidationError("Invalid GAZ PDL. Must start with 'GI' and be 6 characters long.")
        elif data['entre'] == 'ELEC' and len(data['pdl']) != 14:
            raise serializers.ValidationError("Invalid ELEC PDL. Must be 14 characters long.")
        return data