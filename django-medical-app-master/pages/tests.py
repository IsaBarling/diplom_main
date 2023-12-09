from django.test import TestCase
from django.urls import reverse
from .models import Patient, Disease, MedicalRecord


class PatientTests(TestCase):

    def test_patient_creation(self):
        Patient.objects.create(
            name='John Doe',
            email='john@example.com',
            age=30
        )
        self.assertEqual(Patient.objects.count(), 1)


class ViewsTests(TestCase):

    def test_homepage_view(self):
        url = reverse('homepage')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_create_record_view(self):
        self.client.login(username='testuser', password='12345')

        disease = Disease.objects.create(name='Flu')
        url = reverse('create-record')

        data = {'disease': disease.id, 'diagnosis_date': '2023-03-06'}

        response = self.client.post(url, data)

        record = MedicalRecord.objects.last()
        self.assertEqual(record.disease, disease)
