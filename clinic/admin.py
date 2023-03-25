from django.contrib import admin

# Register your models here.

from . models import Patient,Doctor,Appointment,HealthHistory,PatientVisit,MedicalHistory

# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(HealthHistory)
admin.site.register(PatientVisit)
admin.site.register(MedicalHistory)
