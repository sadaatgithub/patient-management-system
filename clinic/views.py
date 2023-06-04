from django.shortcuts import render
from . models import Patient,PatientVisit,Appointment,Prescription,Doctor
from datetime import datetime

# Create your views here.
from .serializers import PatientSerializers,PatientVisitSerializers,\
    AppointmentSerializers,PrescriptionSerializers,EachPatientVisitSerializer \
        ,UpdateAppointmentStatusSerializer,PrescriptionDetailSerializers, DoctorSerializer

from rest_framework.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeViewSet(ModelViewSet):
    serializer_class = PatientSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()
    
class PatientVisitView(ModelViewSet):
    
    serializer_class = PatientVisitSerializers
    permission_classes = [IsAuthenticated]

    # queryset = PatientVisit.objects.select_related('patient_visit').all()

    def get_queryset(self):
        return PatientVisit.objects.all()

class AppointmentViewSet(ModelViewSet):
    # http_methods = ['get','post','patch']
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        now = datetime.now()
        return Appointment.objects.filter(date_requested=now).all()
    
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateAppointmentStatusSerializer
        return AppointmentSerializers


class PrescriptionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    # serializer_class = PrescriptionSerializers
    queryset = Prescription.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PrescriptionDetailSerializers
        return PrescriptionSerializers


class EachPatientVisitViewSet(ModelViewSet):
    serializer_class = EachPatientVisitSerializer
    permission_classes = [IsAuthenticated]


   
    def get_queryset(self):
        print(self.kwargs)
        return PatientVisit.objects.filter(patient=self.kwargs['patient_id_pk'])
    
class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]



    
# class SingleApiView(ReadOnlyModelViewSet):
#     serializer_class = InitialDataSerializer
#     queryset = []

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = InitialDataSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get_queryset(self):
#         return self.queryset