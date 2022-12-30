# Generated by Django 4.1.1 on 2022-12-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_doctor_phone_number_alter_nurse_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='phone_number',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_phone_number',
            field=models.CharField(default=None, max_length=15),
        ),
    ]