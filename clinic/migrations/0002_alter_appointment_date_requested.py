# Generated by Django 4.1.7 on 2023-03-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_requested',
            field=models.DateField(default=''),
        ),
    ]