"""
Views for image requests.
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView

from .models import (
    Patient,
    Tomography
)
from .serializers import (
    TomographySerializer,
    PatientSerializer
)

class AddTomographyView(APIView):
    serializer_class = TomographySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        patient_id = self.request.query_params.get("patient_id")
        if not patient_id:
            return Response({'status': 'error', 'message': 'patient_id should be passed'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({'status': 'error', 'message': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TomographySerializer(data=request.data, context={'request': request, 'doctor': request.user})
        if serializer.is_valid():
            #values = self.format_results(request.data)
            #self.send_tomography_to_sheets(values)
            serializer.save(patient=patient)
            response = {'status': 'success',
                        'message': 'Tomography added successfully',
                        'data': serializer.data,
                        'patient': patient.full_name
                        }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {'status': 'error',
                        'message': serializer.errors,
                        }
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({'status': 'error', 'message': 'patient_id should be passed'}, status=status.HTTP_400_BAD_REQUEST)

class ReadDestroyTomographyDetailView(RetrieveAPIView, DestroyAPIView):
    queryset = Tomography.objects.all()
    serializer_class = TomographySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        tomography_id = self.kwargs.get('pk')
        return get_object_or_404(Tomography, id=tomography_id)

    def retrieve(self, request, *args, **kwargs):
        tomography = self.get_object()
        serializer = self.get_serializer(tomography)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        tomography = self.get_object()
        tomography.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListTomographyView(ListAPIView):
    queryset = Tomography.objects.all()
    serializer_class = TomographySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        doctor = user
        patients = Patient.objects.filter(doctor=doctor)
        queryset = Tomography.objects.filter(patient__in=patients)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'status': "success",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        response = {
            'status': "success",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(doctor=request.user)
        response = {
            'status': "success",
            'message': "Patient created successfully",
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)

