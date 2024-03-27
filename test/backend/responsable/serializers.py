from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import phonenumbers

class ResponsableSerializer(serializers.ModelSerializer):
    entreprise_id = serializers.PrimaryKeyRelatedField(queryset=Entreprise.objects.all(), source='entreprise',
                                                       write_only=True)
    class Meta:
        model = Responsable
        fields = ['first_name', 'last_name', 'email', 'phone_number','entreprise_id']


    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")
        return value

    def validate_phone_number(self, value):
        try:
            phone_number = phonenumbers.parse(value)
            if not phonenumbers.is_valid_number(phone_number):
                raise serializers.ValidationError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise serializers.ValidationError("Invalid phone number")
        return value