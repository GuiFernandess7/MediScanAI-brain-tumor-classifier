from django.db import models
from django.core.validators import RegexValidator
from access.models import Doctor
import uuid
import os

def image_file_path(instance, filename):
    """Generate file path for new image"""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return f'tomography_images/{filename}'

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False, blank=False)
    registration_number = models.IntegerField(auto_created=False)
    full_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15,
                           validators=[RegexValidator(regex=r'\d{3}\.\d{3}\.\d{3}\-\d{2}',
                                                       message='CPF must be in the format XXX.XXX.XXX-XX', code='invalid_cpf')]
                        )

    def __str__(self):
        return self.full_name

class Tomography(models.Model):
    CATEGORY_CHOICES = [
        ('Brain', 'Brain'),
    ]
    image = models.ImageField(upload_to=image_file_path, blank=False, null=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=False, null=False)
    results = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='tomographies', null=True, blank=True)

    def __str__(self):
        return f'{self.category}-{self.creation_date}'
