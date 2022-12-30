
from django import forms
from accounts import models

class Createpatient(forms.ModelForm):
    class Meta:
        model = models.patient
        fields = [
            'patient_id',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'date_of_birth',
            'age',
            'patient_phone_number', 
            'complaint', 
            'condition_of_complaint',
            'assigned_doctor',
            'user', 
            ]

class Createdoctor(forms.ModelForm):
    class Meta:
        model = models.doctor
        fields = [
            'doctor_id',
            'first_name',
            'last_name',
            'middle_name',
            'email' ,
            'password',
            'address',
            'date_of_birth',
            'age',
            'phone_number', 
            'department_code', 
            'doctor_type', 
            'user', ]

            


class Createnurse(forms.ModelForm):
    class Meta:
        model = models.nurse
        fields = [
            'nurse_id',
            'first_name',
            'last_name',
            'middle_name',
            'address',
            'date_of_birth',
            'age',
            'phone_number', 
            'department_code', 
            'nurse_type', 
            'user',

            
            ]

class Createpriscription(forms.ModelForm):
    class Meta:
        model = models.priscription
        fields = [
            'patient_id',
            'doctor_id',
            'priscription_id',
            'discription',
            


            ]



class Createmedication(forms.ModelForm):
    class Meta:
        model = models.medication
        fields = [
            'drug_id',
            'drug_name',
            'drug_brand',
            'drug_ammount',
            'drug_discription',
            ]



class Createdepartment(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = [
            'department_code',
            'department_name',
            'head_of_department',
            ]


class Createappointment(forms.ModelForm):
    class Meta:
        model = models.appointment
        fields = [
            'appointment_id',
            'patient_id',
            'consultant_id',
            'date_of_appointment',
            'priscription_id',
            ]




class Createpyments(forms.ModelForm):
    class Meta:
        model = models.payments
        fields = [
            'payment_id',
            'date_of_payment',
            'patient_id',
            'appointment_ammount',
            'medication_ammount',
            'service_ammount',
            'payment_status',
            'priscription_id',
            ]




class Createroom(forms.ModelForm):
    class Meta:
        model = models.room
        fields = [
            'room_id',
            'room_type',
            'room_capasity',
            'department_assigned',
            ]