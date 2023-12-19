
from django.views.generic import ListView, TemplateView
from pages.models import MedicalRecord


class HomePageView(TemplateView):
    template_name = 'templates/landing_page.html'


class StatPageView(ListView):
    model = MedicalRecord
    template_name = 'templates/stat.html'
