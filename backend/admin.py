from django.contrib import admin
from .models import DoctorDetails, PatientDetails, Records, Chat

# Register your models here.
admin.site.register(DoctorDetails)
admin.site.register(PatientDetails)
admin.site.register(Records)
admin.site.register(Chat)
