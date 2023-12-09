from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Disease(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    summary = models.TextField()