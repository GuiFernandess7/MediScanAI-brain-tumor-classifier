from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

class AuthenticationTest(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')

    def test_successful_registration(self):
        data = {
            'email': 'test@example.com',
            'full_name': 'Test User',
            'password': 'testpassword',
            'crm': '000000/SP'
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_without_crm(self):
        data = {
            'email': 'test2@example.com',
            'full_name': 'Test User 2',
            'password': 'testpassword'
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['crm'], ['This field is required.'])

    def test_registration_without_full_name(self):
        data = {
            'email': 'test3@example.com',
            'password': 'testpassword',
            'crm': '000001/SP'
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['full_name'], ['This field is required.'])

    def test_registration_with_invalid_crm_format(self):
        data = {
            'email': 'test4@example.com',
            'full_name': 'Test User 4',
            'password': 'testpassword',
            'crm': '000001SP'
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('crm', response.data)
        self.assertIn('CRM must be in the format', response.data['crm'][0])

    def test_successful_login(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            full_name='Test User',
            password='testpassword',
            crm='000000/SP'
        )
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'crm': '000000/SP'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data.keys())

    def test_login_with_invalid_email(self):
        data = {
            'email': 'invalid@example.com',
            'password': 'testpassword',
            'crm': '000000/SP',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_invalid_password(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            full_name='Test User',
            password='testpassword',
            crm='000000/SP'
        )
        data = {
            'email': 'test@example.com',
            'password': 'invalidpassword'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
