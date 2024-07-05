"""
Doctor custom models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('Doctor must have an email address.')
        if 'crm' not in extra_fields:
            raise ValueError('Doctor must have a CRM')
        if 'full_name' not in extra_fields:
            raise ValueError('Doctor full name is necessary.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a new doctor."""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Doctor(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    crm = models.CharField(max_length=9,
                           validators=[
                               RegexValidator(regex=r'^\d{6}/[A-Z]{2}$',
                                              message='Invalid CRM',
                                              code='invalid_crm')])
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'