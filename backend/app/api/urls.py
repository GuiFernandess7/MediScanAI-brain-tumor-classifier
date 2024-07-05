from django.urls import path, include
from rest_framework import routers
from .views import (
    PatientViewSet,
    AddTomographyView,
    ReadDestroyTomographyDetailView,
    ListTomographyView
)

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/add-tomography/', AddTomographyView.as_view(), name="add-tomography-v1"),
    path('v1/tomographies/', ListTomographyView.as_view(), name="list-tomographies-v1"),
    path('v1/tomographies/<int:pk>', ReadDestroyTomographyDetailView.as_view(), name="read-destroy-tomography-v1"),
]
