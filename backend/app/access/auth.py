from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CRMAuthenticationBackend(ModelBackend):
    def authenticate(self, request, crm=None, password=None, **kwargs):
        if crm is None:
            return None

        try:
            user = get_user_model().objects.get(crm=crm)
        except user.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
