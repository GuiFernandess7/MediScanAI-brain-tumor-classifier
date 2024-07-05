from django.contrib import admin
from .models import Patient, Tomography

admin.site.register(Patient)
admin.site.register(Tomography)