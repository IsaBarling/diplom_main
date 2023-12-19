
from django.views.generic import ListView, TemplateView
from pages.models import MedicalRecord


class HomePageView(TemplateView):
    template_name = 'landing_page.html'


class StatPageView(ListView):
    model = MedicalRecord
    template_name = 'stat.html'
