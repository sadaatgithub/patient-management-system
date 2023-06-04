from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("other","Other")
)
BLOOD_GROUP_CHOICES = (
    ('A +ve', 'A +ve'),
    ('A -ve', 'A -ve'),
    ('B +ve', 'B +ve'),
    ('B -ve', 'B -ve'),
    ('O +ve', 'O +ve'),
    ('O -ve', 'O -ve'),
    ('AB +ve', 'AB +ve'),
    ('AB -ve', 'AB -ve'),
    )
MARRITAL_STATUS =(
    ("Married","Married"),
("Unmarried","Unmarried"),
)

HEIGHT_CHOICES=(
    ("150","150"),
    ("155","155"),
    ("160","160"),
    ("165","165"),
    ("170","170"),
    ("175","175"),
    ("180","180"),
    ("185","185"),
    ("190","190"),
    ("195","195"),
    ("200","200"),
    ("205","205"),
    ("210","210"),
    ("215","215"),
    ("220","220"),
)

def generate_unique_id():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp

class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "User"

class BaseInfo(models.Model):
    id_number = models.CharField(max_length=200,default=generate_unique_id, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    dob = models.DateField(auto_now_add=False,auto_now=False)
    blood_group = models.CharField(max_length=20,choices=BLOOD_GROUP_CHOICES)
    marrital_status = models.CharField(max_length=20, choices=MARRITAL_STATUS)

    class Meta:
        abstract = True

class AddressWithBase(BaseInfo):
    line_one = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=200)

    class Meta:
        abstract = True

    # def __str__(self):
    #     return self.line_one

class Patient(AddressWithBase):
    date_recorded = models.DateTimeField(default=timezone.now)
    pt_height = models.CharField(max_length=50,choices=HEIGHT_CHOICES,default="")
    pt_weight = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Doctor(BaseInfo):
    position = models.CharField(max_length=100, default="Doctor")

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescribed_drug = models.CharField(max_length=100)
    prescribed_on = models.DateTimeField(default=timezone.now)
    prescription_notes = models.TextField()

    def __str__(self):
        return self.patient.first_name + " "+ str(self.prescribed_drug)
    
class Appointment(models.Model):
    id_number = models.CharField(max_length=200,default=generate_unique_id,unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField(null=True)
    date_requested = models.DateField(default="")
    approved = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="visits")
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.first_name

class PatientBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="bills")
    treatment_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    payment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.patient.first_name
    
class HealthHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="health_history")
    history = models.TextField()

    def __str__(self):
        return self.patient.first_name
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="medical_history")
    known_disease = models.CharField(max_length=200,null=True,default="NA")
    period = models.CharField(max_length=50,null=True,default="NA")
    family_history = models.CharField(max_length=100,null=True,default="NA")

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name 