"""
Tests for user models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from django.test import Client

from django.core.exceptions import ValidationError

class ModelTests(TestCase):
    """Test creating a doctor with an email successfully."""

    def test_create_doctor_successfully(self):
        """Test creating doctor with an email successfully."""
        email = "test@example.com"
        password = "testpass123"
        full_name = "Test"
        crm = "000000/SP"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
            crm=crm
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.crm, crm)
        self.assertTrue(user.check_password(password))

    def test_missing_full_name(self):
        """Test missing full name."""
        email = "test@example.com"
        password = "testpass123"
        crm = "000000/SP"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password,
                crm=crm
            )

    def test_missing_crm(self):
        """Test missing CRM."""
        email = "test@example.com"
        password = "testpass123"
        full_name = "Test"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password,
                full_name=full_name
            )
