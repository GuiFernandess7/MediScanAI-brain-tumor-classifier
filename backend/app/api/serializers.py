"""
API models serializers.
"""
from rest_framework import serializers
from tempfile import NamedTemporaryFile
import os

import numpy as np

from api.models import (
    Tomography,
    Patient,
)

from api.ggsheets import set_sheet

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
            values = self.format_results(validated_data['results'], validated_data)
            self.send_tomography_to_sheets(values)

    def calculate_image_results(self, instance):
        from .preprocessing.brain.preprocess_image import get_image_results
        results = get_image_results(instance, target_size=(150, 150))
        return results

    def format_results(self, data: str, validated_data):
        from datetime import datetime
        request = self.context['request']
        array_float = np.round(data, decimals=2)
        array_float = array_float.astype(float)
        glioma, meningioma, no_tumor, pituitary = array_float[0]
        category = validated_data['category']
        patient_id = request.query_params.get('patient_id')
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        row = [category,
               round(pituitary, 3),
               round(meningioma, 3),
               round(glioma, 3),
               round(no_tumor, 3),
               creation_time,
               patient_id
            ]
        return row

    def send_tomography_to_sheets(self, row):
        try:
            worksheet = set_sheet(sheet_name="Tomografias")
            worksheet.append_row(row)
        except Exception as e:
            raise ValueError(f"Error adding tomography to Google Sheets: {e}")

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'registration_number', 'full_name', 'cpf')
        read_only_fields = ('id',)

    def perform_create(self, validated_data):
        user = self.context['request'].user
        validated_data['doctor_id'] = user
        return super().create(validated_data)
