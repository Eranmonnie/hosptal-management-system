# Generated by Django 4.1.1 on 2022-12-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_patient_patient_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='condition_of_complaint',
            field=models.CharField(choices=[('1', 'inpatient'), ('2', 'outpatient')], default='2', max_length=2),
        ),
    ]
