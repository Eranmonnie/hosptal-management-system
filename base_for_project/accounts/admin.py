from django.contrib import admin
from .models import patient, doctor, nurse, medication, Department, room, appointment, payments, priscription

admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(nurse)
admin.site.register(medication)
admin.site.register(Department)
admin.site.register(room)
admin.site.register(appointment)
admin.site.register(payments)
admin.site.register(priscription)

