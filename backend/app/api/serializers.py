"""
API models serializers.
"""
from rest_framework import serializers
from tempfile import NamedTemporaryFile
import os

from api.models import (
    Tomography,
    Patient,
)

class TomographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tomography
        fields = ('id', 'category', 'image', 'results',)
        read_only_fields = ('id', 'created_at', 'results')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, validated_data):
        image = validated_data['image']
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(image.read())

        try:
            resultados = self.calculate_image_results(temp_file.name)
            validated_data['results'] = resultados
            return super().create(validated_data)
        finally:
            os.remove(temp_file.name)

    def calculate_image_results(self, instance):
        from .preprocessing.brain.preprocess_image import get_image_results
        results = get_image_results(instance, target_size=(150, 150))
        return results

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'registration_number', 'full_name', 'cpf')
        read_only_fields = ('id',)

    def perform_create(self, validated_data):
        user = self.context['request'].user
        validated_data['doctor_id'] = user
        return super().create(validated_data)
