from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from api.models import Tomography, Patient

class TomographyTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email='testuser@email.com', password='testpassword', crm='000000/SP', full_name='Doctor Doe')
        self.client.force_authenticate(user=self.user)
        self.patient = Patient.objects.create(doctor=self.user, registration_number='123456', full_name='John Doe', cpf='123.456.789-00')

    def test_list_tomographies(self):
        url = reverse('list-tomographies-v1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_tomography(self):
        tomography = Tomography.objects.create(patient=self.patient, category='Brain', image='./tumor.jpg', results='Results')
        url = reverse(f'read-destroy-tomography-v1', kwargs={'pk': tomography.pk})
        response = self.client.get(f"{url}?id={tomography.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_tomography(self):
        tomography = Tomography.objects.create(patient=self.patient, category='Brain', image='./tumor.jpg', results='Results')
        url = reverse('read-destroy-tomography-v1', kwargs={'pk': tomography.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Tomography.objects.filter(pk=tomography.pk).exists())

    """ def test_create_tomography(self):
        patient = Patient.objects.create(doctor_id=self.user.id ,registration_number='654321', full_name='Jane Doe', cpf='987.654.321-00')
        url = reverse('add-tomography-v1', args={"patient_id": patient.id})
        data = {
            'category': 'Brain',
            'image': './tumor.jpg',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) """