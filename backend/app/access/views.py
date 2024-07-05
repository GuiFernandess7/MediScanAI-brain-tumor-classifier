from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import (
    SignUpSerializer
)
from .tokens import (
    create_jwt_pair_for_user
)
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
#from .auth import CRMAuthenticationBackend


class SignUpView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Doctor Registered Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        crm = request.data.get("crm")

        if not crm:
            return Response(data={"message": "CRM must be informed"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request=request, crm=crm, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login Successfull",
                "tokens": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data={"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)

