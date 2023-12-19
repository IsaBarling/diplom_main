from django.contrib import admin
from .models import Patient, Doctor

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'  

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'disease', 'diagnosis_date']
    list_filter = ('disease', 'diagnosis_date')
