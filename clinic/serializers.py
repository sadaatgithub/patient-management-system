from rest_framework import serializers
from collections import OrderedDict

from . models import Patient, PatientVisit, Appointment, Prescription,Doctor,MedicalHistory,HealthHistory
from datetime import datetime

class SimplePatientSerializers(serializers.ModelSerializer):
    id_number = serializers.CharField(read_only=True)
    # phone = serializers.CharField(read_only=True)
    # last_name = serializers.CharField(read_only=True)
    class Meta:
        model = Patient
        fields = ['id','phone','last_name','id_number']
    

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id_number','phone']

class MedicalHistorySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        read_only_fields = ['patient']
        


class PatientHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthHistory
        fields = '__all__'

class PatientSerializers(serializers.ModelSerializer):

    id_number = serializers.CharField(read_only=True)
    # health_history = PatientHistorySerializers(many=True,read_only=True)
    medical_history = MedicalHistorySerializers(many=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
    date_joined = serializers.SerializerMethodField(method_name="joined_date_only")

    def joined_date_only(self,Patient:Patient):
        date_string = str(Patient.date_recorded)[:10]
        return date_string
    
    def create(self,validated_data):
        medical_history = validated_data.pop('medical_history')
        medical_history_dict = dict(medical_history[0])
        patient = Patient.objects.create(**validated_data)
        MedicalHistory.objects.create(patient=patient,**medical_history_dict)
        PatientVisit.objects.create(patient=patient)
        return patient

    def update(self,instance,validated_data):
        medical_history= validated_data.pop('medical_history')
        medical_history_data = dict(medical_history[0])
  
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.email = validated_data.get('email',instance.email)
        instance.dob = validated_data.get('dob',instance.dob)
        instance.blood_group = validated_data.get('blood_group',instance.blood_group)
        instance.marrital_status = validated_data.get('marrital_status',instance.marrital_status)
        instance.line_one = validated_data.get('line_one',instance.line_one)
        instance.zip_code = validated_data.get('zip_code',instance.zip_code)
        instance.city = validated_data.get('city',instance.city)
        instance.country = validated_data.get('country',instance.country)

        # print(instance.medical_history.get(id=1))
        history = instance.medical_history.get(id=medical_history_data.get('id'))
        # print(history)
        history.known_disease = medical_history_data.get('known_disease', history.known_disease)
        history.period = medical_history_data.get('period', history.period)
        history.save()
        instance.save()
        return instance


class PatientVisitSerializers(serializers.ModelSerializer):
    id_number = serializers.CharField(read_only=True)

    
    class Meta:
        model = PatientVisit
        fields = ['id','patient','visit_date','id_number']
    

class AppointmentSerializers(serializers.ModelSerializer):
    id_number = serializers.CharField(read_only=True)


    class Meta:
        model = Appointment
        fields = '__all__'


class PrescriptionSerializers(serializers.ModelSerializer):
    # patient = SimplePatientSerializers(read_only=True)
    # prescribed_by = DoctorSerializer(read_only=True)

    class Meta:
        model = Prescription
        fields = ['patient','prescribed_by','prescribed_drug','prescribed_on','prescription_notes']


class EachPatientVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVisit
        fields = '__all__'

# class InitialDataSerializer(serializers.Serializer):
#     patient = PatientSerializers()
#     visits = PatientVisitSerializers()

#     def to_representation(self,instance):
#         patient_data = Patient.objects.all()
#         visit_data = PatientVisit.objects.all()

#         serialized_data={
#             'patient_data':PatientSerializers(patient_data,many=True).data,
#             'visit_data':PatientVisitSerializers(visit_data,many=True).data,

#         }
#         return serialized_data


  
