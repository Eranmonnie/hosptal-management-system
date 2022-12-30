# Generated by Django 4.1.1 on 2022-12-01 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_appointment_user_log_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_phone_number',
            field=models.IntegerField(default=None),
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(default=None, max_length=7)),
                ('room_type', models.CharField(default=None, max_length=50)),
                ('room_capasity', models.IntegerField(default=12)),
                ('department_assigned', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(default=None, max_length=7)),
                ('date_of_paymrnt', models.DateField(default=None, max_length=8)),
                ('appointment_ammount', models.IntegerField(default=None)),
                ('medication_ammount', models.IntegerField(default=None)),
                ('service_ammount', models.IntegerField(default=None)),
                ('payment_status', models.BooleanField(default=False)),
                ('patient_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.patient')),
                ('priscription_id', models.ForeignKey(default=None, max_length=7, on_delete=django.db.models.deletion.CASCADE, to='accounts.priscription')),
            ],
        ),
    ]
