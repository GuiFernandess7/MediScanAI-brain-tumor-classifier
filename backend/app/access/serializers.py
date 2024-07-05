from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.core.validators import RegexValidator
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

from .models import (
    Doctor
)

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    full_name = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)
    crm = serializers.CharField(max_length=9,
                                validators=
                                    [RegexValidator(regex=r'^\d{6}/[A-Z]{2}$',
                                                    message="message='CRM must be in the format '000000/AA'",
                                                    code='invalid_crm'
                                    )
                                ]
                            )

    class Meta:
        model=Doctor
        fields=['email', 'full_name', 'crm', 'password']

    def validate(self, attrs):
        crm_exists = Doctor.objects.filter(crm=attrs['crm']).exists()

        if crm_exists:
            raise ValidationError("CRM has already been used.")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        Doctor = super().create(validated_data)
        Doctor.set_password(password)
        Doctor.save()
        Token.objects.create(user=Doctor)
        return Doctor

