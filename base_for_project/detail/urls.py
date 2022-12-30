from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('patient_create/',views.patient_create, name='patient_d'),
    path('doctor_create/',views.doctor_create, name='doctor_d'),
    path('nurse_create/',views.nurse_create, name='nurse_d'),
    path('medication_create/',views.medication_create, name='medication_d'),
    path('priscription_create/',views.priscription_create, name='priscription_d'),
    path('department_create/',views.department_create, name='department_d'),
    path('appointment_create/',views.appointment_create, name='appointment_d'),
    path('payments_create/',views.payments_create, name='payments_d'),
    path('doctor_details/',views.doctor_details, name='doctor_det'),
    path('nurse_details/',views.nurse_details, name='nurse_det'),
    path('patient_details/',views.patient_details, name='patient_det'),
    path('room_create/',views.room_create, name='room_d')
    
]