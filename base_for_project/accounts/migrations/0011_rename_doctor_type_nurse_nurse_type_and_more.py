# Generated by Django 4.1.1 on 2022-12-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_patient_condition_of_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nurse',
            old_name='doctor_type',
            new_name='nurse_type',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='id',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.DateField(default=None, max_length=8),
        ),
        migrations.AddField(
            model_name='appointment',
            name='priscription_id',
            field=models.ForeignKey(default=None, max_length=7, on_delete=django.db.models.deletion.CASCADE, to='accounts.priscription'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='medication',
            name='drug_id',
            field=models.CharField(default=None, max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(default=None, max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default=None, max_length=7, primary_key=True, serialize=False),
        ),
    ]
