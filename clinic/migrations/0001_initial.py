# Generated by Django 4.1.7 on 2023-03-26 13:35

import clinic.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(default=clinic.models.generate_unique_id, max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'Other')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(default=clinic.models.generate_unique_id, max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'Other')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(choices=[('A +ve', 'A +ve'), ('A -ve', 'A -ve'), ('B +ve', 'B +ve'), ('B -ve', 'B -ve'), ('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('AB +ve', 'AB +ve'), ('AB -ve', 'AB -ve')], max_length=20)),
                ('marrital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=20)),
                ('position', models.CharField(default='Doctor', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(default=clinic.models.generate_unique_id, max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('other', 'Other')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(choices=[('A +ve', 'A +ve'), ('A -ve', 'A -ve'), ('B +ve', 'B +ve'), ('B -ve', 'B -ve'), ('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('AB +ve', 'AB +ve'), ('AB -ve', 'AB -ve')], max_length=20)),
                ('marrital_status', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], max_length=20)),
                ('line_one', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
                ('pt_height', models.CharField(choices=[('150', '150'), ('155', '155'), ('160', '160'), ('165', '165'), ('170', '170'), ('175', '175'), ('180', '180'), ('185', '185'), ('190', '190'), ('195', '195'), ('200', '200'), ('205', '205'), ('210', '210'), ('215', '215'), ('220', '220')], default='', max_length=50)),
                ('pt_weight', models.CharField(default='', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribed_drug', models.CharField(max_length=100)),
                ('prescribed_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('prescription_notes', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
                ('prescribed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('known_disease', models.CharField(default='NA', max_length=200, null=True)),
                ('period', models.CharField(default='NA', max_length=50, null=True)),
                ('family_history', models.CharField(default='NA', max_length=100, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history', to='clinic.patient')),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_history', to='clinic.patient')),
            ],
        ),
    ]
