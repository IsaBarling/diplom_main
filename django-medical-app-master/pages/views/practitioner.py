from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView  
from django.shortcuts import redirect  
from django.contrib.auth import login  
from django.db.models import Q  

from pages.models import Patient, Disease, MedicalRecord, Doctor  

class DoctorSignupView(CreateView):
    model = Doctor  # Убедись, что модель Doctor определена
    fields = ['name', 'email', 'password']
    template_name = 'accounts/practitioner/doctor_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')  

class DoctorLoginView(LoginView):
    template_name = 'accounts/practitioner/doctor_login.html'

class DoctorLogoutView(LogoutView):
    next_page = 'home' 

class PatientListView(LoginRequiredMixin, ListView):
    model = MedicalRecord

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = Q()

        if 'search' in self.request.GET:
            filters &= Q(summary__icontains=self.request.GET['search'])

        if 'disease' in self.request.GET:
            filters &= Q(disease=self.request.GET['disease'])

        return queryset.filter(filters)

    context_object_name = 'patients'
    template_name = 'patient_list.html'
