from django.shortcuts import render
from . models import Patient,PatientVisit,Appointment,Prescription,Doctor
from datetime import datetime
from django.conf import settings

# Create your views here.
from .serializers import PatientSerializers,PatientVisitSerializers,\
    AppointmentSerializers,PrescriptionSerializers,EachPatientVisitSerializer \
        ,UpdateAppointmentStatusSerializer,PrescriptionDetailSerializers, DoctorSerializer

from rest_framework.viewsets import ModelViewSet,GenericViewSet,ReadOnlyModelViewSet
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

class HomeViewSet(ModelViewSet):
    serializer_class = PatientSerializers
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()
    
class PatientVisitView(ModelViewSet):
    
    serializer_class = PatientVisitSerializers
    # permission_classes = [IsAuthenticated]

    # queryset = PatientVisit.objects.select_related('patient_visit').all()

    def get_queryset(self):
        return PatientVisit.objects.all()

class AppointmentViewSet(ModelViewSet):
    # http_methods = ['get','post','patch']
    # permission_classes = [IsAuthenticated]


    def get_queryset(self):
        now = datetime.now()
        return Appointment.objects.filter(date_requested=now).all()
    
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateAppointmentStatusSerializer
        return AppointmentSerializers


class PrescriptionViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]

    # serializer_class = PrescriptionSerializers
    queryset = Prescription.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PrescriptionDetailSerializers
        return PrescriptionSerializers


class EachPatientVisitViewSet(ModelViewSet):
    serializer_class = EachPatientVisitSerializer
    # permission_classes = [IsAuthenticated]


   
    def get_queryset(self):
        print(self.kwargs)
        return PatientVisit.objects.filter(patient=self.kwargs['patient_id_pk'])
    
class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    # permission_classes = [IsAuthenticated]

# --------------------------------------------------------------------->

# Custom djoser views----------------------------------->

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return response
    
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response
