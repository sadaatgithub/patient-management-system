from django.contrib import admin

# Register your models here.

from . models import User,Patient,Doctor,Appointment,HealthHistory,PatientVisit,MedicalHistory,Prescription
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(HealthHistory)
admin.site.register(PatientVisit)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )
