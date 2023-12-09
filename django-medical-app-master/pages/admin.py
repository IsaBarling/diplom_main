from django.contrib import admin
from .models import Patient, Doctor, MedicalRecord, Disease


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'disease', 'diagnosis_date']
    list_filter = ('disease', 'diagnosis_date')