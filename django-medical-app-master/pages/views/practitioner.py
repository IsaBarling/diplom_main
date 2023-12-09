from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Doctor, Patient, MedicalRecord, Disease


class DoctorSignupView(CreateView):
    model = Doctor
    fields = ['name', 'email', 'password']
    template_name = 'doctor_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class DoctorLoginView(LoginView):
    template_name = 'doctor_login.html'


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