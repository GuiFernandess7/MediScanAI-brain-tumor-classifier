from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Patient
from django.contrib.auth import get_user_model

class PatientViewSetTests(APITestCase):
    def setUp(self):
        doctor = get_user_model()
        self.user = doctor.objects.create_user(email='testuser@email.com', password='testpassword', crm='000000/SP', full_name='Doctor Doe')
        self.client.force_authenticate(user=self.user)

    def test_create_patient(self):
        url = reverse('patient-list')
        data = {
            'registration_number': '123456',
            'full_name': 'John Doe',
            'cpf': '123.456.789-00'
        }
        data['doctor_id'] = self.user.id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().full_name, 'John Doe')

    def test_retrieve_patient(self):
        patient = Patient.objects.create(doctor_id=self.user.id ,registration_number='654321', full_name='Jane Doe', cpf='987.654.321-00')
        url = reverse('patient-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"][0]['full_name'], 'Jane Doe')

    def test_update_patient(self):
        patient = Patient.objects.create(doctor_id=self.user.id ,registration_number='654321', full_name='Jane Doe', cpf='987.654.321-00')
        url = reverse('patient-detail', args=[patient.id])
        updated_data = {'full_name': 'Updated Name'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'Updated Name')

    def test_delete_patient(self):
        patient = Patient.objects.create(doctor_id=self.user.id, registration_number='654321', full_name='Jane Doe', cpf='987.654.321-00')
        url = reverse('patient-detail', args=[patient.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)

    def test_missing_information(self):
        url = reverse('patient-list')
        data = {
            'full_name': 'John Doe',
            'cpf': '123.456.789-00'
        }
        data['doctor_id'] = self.user.id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_cpf_format(self):
        url = reverse('patient-list')
        data = {
            'registration_number': '123456',
            'full_name': 'John Doe',
            'cpf': 'invalid_cpf_format'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
