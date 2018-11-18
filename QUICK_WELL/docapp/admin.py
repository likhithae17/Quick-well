from django.contrib import admin
from .models import Specialization, Doctor, Qualification,Hospital_Affiliation, Office, Office_Docavailability, User,User_Review,Appointment, Appointment_Status, LabTest, Tests_info

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Hospital_Affiliation)
admin.site.register(Office)
admin.site.register(Office_Docavailability)
admin.site.register(User)
admin.site.register(User_Review)
admin.site.register(Appointment)
admin.site.register(Appointment_Status)
admin.site.register(LabTest)
admin.site.register(Tests_info)