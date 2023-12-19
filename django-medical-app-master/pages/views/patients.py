from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView  
from django.views.generic import CreateView
from django.shortcuts import redirect  
from django.contrib.auth import login  

from pages.models import Patient, Disease, MedicalRecord

class PatientSignUpView(CreateView):
    model = Patient
    fields = ['name', 'email', 'password']
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')

class PatientLoginView(LoginView):
    template_name = 'login.html'

class MedicalRecordCreateView(LoginRequiredMixin, CreateView):
    model = MedicalRecord
    fields = ['disease', 'diagnosis_date', 'summary']
    template_name = 'create_record.html'

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)
