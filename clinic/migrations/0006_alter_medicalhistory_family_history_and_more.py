# Generated by Django 4.1.7 on 2023-03-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_alter_medicalhistory_family_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='family_history',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='known_disease',
            field=models.CharField(default='NA', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='period',
            field=models.CharField(default='NA', max_length=50, null=True),
        ),
    ]
