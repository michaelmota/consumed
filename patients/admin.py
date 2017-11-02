from django.contrib import admin
from .models import Doctor, PatientProfile, ClinicHistory, Therapy

# Register your models here.

admin.site.register(Doctor)
admin.site.register(PatientProfile)
admin.site.register(ClinicHistory)
admin.site.register(Therapy)
