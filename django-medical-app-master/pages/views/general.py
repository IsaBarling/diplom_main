
from django.views.generic import ListView, TemplateView
from pages.models import MedicalInfo


class HomePageView(TemplateView):
    template_name = 'pages/landing_page.html'


class StatPageView(ListView):
    model = MedicalInfo
    template_name = 'pages/stat.html'
