from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('patient/',views.patient, name='patien_dd'),
    path('Doctor/', views.doctor, name='doctor_dd' ),
    path('nurse/', views.doctor, name='nurse_dd' ),
]