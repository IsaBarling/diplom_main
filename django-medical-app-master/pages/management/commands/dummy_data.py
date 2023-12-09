import datetime
import random
from faker import Faker

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from pages.models import Patient, Disease, MedicalRecord


class Command(BaseCommand):
    help = 'Generates test data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=100, help='The number of users to create')
        parser.add_argument('--records', type=int, default=500, help='The number of records to create')

    def handle(self, *args, **options):
        fake = Faker()

        # Создаем пользователей
        for _ in range(options['users']):
            user = fake.simple_profile()
            User.objects.create_user(username=user['username'],
                                     email=user['mail'],
                                     password=user['username'])

        users = User.objects.all()

        # Создаем болезни
        for _ in range(20):
            Disease.objects.create(
                name=fake.disease()
            )

        diseases = Disease.objects.all()

        # Создаем медицинские карты
        for _ in range(options['records']):
            user = random.choice(users)
            disease = random.choice(diseases)

            MedicalRecord.objects.create(
                patient=user,
                disease=disease,
                diagnosis_date=fake.date_between(start_date='-5y', end_date='today'),
                summary=fake.text()
            )

        self.stdout.write(
            self.style.SUCCESS(f'{options["users"]} users and {options["records"]} medical records created!'))