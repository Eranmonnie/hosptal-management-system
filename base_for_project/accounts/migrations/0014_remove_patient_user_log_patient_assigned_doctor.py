# Generated by Django 4.1.1 on 2022-12-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_rename_parient_id_appointment_patient_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user_log',
        ),
        migrations.AddField(
            model_name='patient',
            name='assigned_doctor',
            field=models.CharField(default=None, max_length=7),
        ),
    ]
