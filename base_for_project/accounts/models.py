from django.db import models 
from django.contrib.auth.models import User
import datetime

class doctor (models.Model):
    doctor_id = models.CharField(max_length=7, primary_key=True, default=None)
    user = models.ForeignKey(User, default= None, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100 , default=None)
    address = models.CharField(max_length = 100)
    date_of_birth = models.DateField(max_length=8, default=None)
    age= models.IntegerField (default=None)
    phone_number= models.CharField(default=None, max_length=15)
    department_code= models.CharField(max_length=7)
    doctor_type = models.CharField(max_length=50)
    password = models.CharField(max_length=10, default=None)
    
    def __str__(self):
        return self.doctor_id


    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or today.month == self.date_of_birth.month and today.day < self.date_of_birth.day:
            age -= 1
        return self.age 



class patient (models.Model):
    patient_id = models.CharField(max_length=7, primary_key=True, default=None)
    user = models.ForeignKey(User, default= None, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    date_of_birth = models.DateField(max_length=8, default=None)
    age= models.IntegerField (default=None)
    assigned_doctor = models.ForeignKey(doctor, default=None, on_delete=models.CASCADE)
    class type(models.TextChoices):
        in_patient = '1', 'inpatient'
        out_patient = '2', 'outpatient'

    patient_type= models.CharField(
        max_length=2,
        choices = type.choices,
        default= type.out_patient
        )

    patient_phone_number = models.CharField(default=None, max_length=15)
    complaint= models.TextField(default=None)

    class condition(models.TextChoices):
        normal = '1', 'normal'
        severe = '2', 'severe'
        extremelty_severe = '3', 'extremely severe'

    condition_of_complaint = models.CharField(
        max_length=3,
        choices = condition.choices,
        default= condition.normal
        )
   
    def __str__(self):
        return self.patient_id


    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or today.month == self.date_of_birth.month and today.day < self.date_of_birth.day:
            age -= 1
        return self.age 




class nurse (models.Model):
    nurse_id = models.CharField(max_length=7, primary_key=True, default=None)
    user = models.ForeignKey(User, default= None, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    date_of_birth = models.DateField(max_length=8, default=None)
    age= models.IntegerField (default=None)
    phone_number= models.CharField(default=None, max_length=1000000000)
    department_code= models.CharField(max_length=7)
    nurse_type = models.CharField(max_length=50)
    password = models.CharField(max_length=10, default=None)
    

    def __str__(self):
        return self.nurse_id


    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or today.month == self.date_of_birth.month and today.day < self.date_of_birth.day:
            age -= 1
        return self.age 



class priscription(models.Model):
    patient_id = models.ForeignKey(patient, default=None, on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(doctor, default=None, on_delete = models.CASCADE)
    priscription_id= models.CharField(max_length=7, primary_key=True, default=None)
    discription = models.TextField(default=None)

    def __str__(self):
        return self.priscription_id

class medication (models.Model):
    drug_id = models.CharField(max_length=7, default=None, primary_key=True)
    drug_name = models.TextField(default=None)
    drug_brand = models.TextField(default=None)
    drug_ammount = models.IntegerField(default=None)
    drug_discription = models.TextField(default=None)

    def __str__(self):
        return self.drug_id




class Department(models.Model):
    department_code = models.CharField(max_length=50, primary_key=True)
    department_name = models.CharField(max_length=50)
    head_of_department= models.ForeignKey(doctor, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.department_code

    
    


class appointment(models.Model):
    appointment_id = models.CharField(max_length=50, primary_key=True)
    patient_id = models.ForeignKey(patient, default=None, on_delete = models.CASCADE)
    consultant_id = models.ForeignKey(doctor, default=None, on_delete = models.CASCADE)
    date_of_appointment = models.DateField(max_length=8, default=None)
    priscription_id = models.ForeignKey(priscription, max_length=7, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.appointment_id

    



class payments(models.Model):
    payment_id = models.CharField(max_length = 7, default = None, primary_key=True)
    date_of_payment = models.DateField(max_length = 8, default=None)
    patient_id = models.ForeignKey(patient, default = None, on_delete = models.CASCADE)
    appointment_ammount = models.IntegerField(default = None)
    medication_ammount = models.IntegerField(default = None)
    service_ammount = models.IntegerField(default = None)
    payment_status = models.BooleanField(default = False)
    priscription_id = models.ForeignKey(priscription, max_length=7, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.payment_id


    def total_ammount(self):
        return self.appointment_ammount + self.medication_ammount + self.service_ammount
            
class room(models.Model):
    room_id = models.CharField(max_length=7, default=None, primary_key=True)
    room_type = models.CharField(default=None, max_length=50)
    room_capasity = models.IntegerField(default=12)
    department_assigned = models.ForeignKey(Department, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.room_id





