from django.shortcuts import render
from . models import Patient,PatientVisit,Appointment,Prescription
# Create your views here.
from .serializers import PatientSerializers,PatientVisitSerializers,\
    AppointmentSerializers,PrescriptionSerializers,EachPatientVisitSerializer

from rest_framework.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,CreateModelMixin
from rest_framework.response import Response



class HomeViewSet(ModelViewSet):
    serializer_class = PatientSerializers

    def get_queryset(self):
        return Patient.objects.all()
    
class PatientVisitView(ModelViewSet):
    
    serializer_class = PatientVisitSerializers
    # queryset = PatientVisit.objects.select_related('patient_visit').all()

    def get_queryset(self):
        return PatientVisit.objects.all()

class AppointmentViewSet(ModelViewSet):

    serializer_class = AppointmentSerializers

    def get_queryset(self):
        return Appointment.objects.all()


class PrescriptionViewSet(ModelViewSet):
    serializer_class = PrescriptionSerializers
    queryset = Prescription.objects.select_related('patient').all()


class EachPatientVisitViewSet(ModelViewSet):
    serializer_class = EachPatientVisitSerializer

   
    def get_queryset(self):
        print(self.kwargs)
        return PatientVisit.objects.filter(patient=self.kwargs['patient_id_pk'])
    

# class SingleApiView(ReadOnlyModelViewSet):
#     serializer_class = InitialDataSerializer
#     queryset = []

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = InitialDataSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get_queryset(self):
#         return self.queryset