from django.urls import path
from pages.views.general import StatPageView, HomePageView
from pages.views.patients import PatientSignUpView, PatientLoginView, MedicalRecordCreateView
from pages.views.practitioner import (
    DoctorLoginView,
    DoctorLogoutView,
    DoctorSignupView,
    )

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('stat/', StatPageView.as_view(), name='stat_page'),
    path('report/', MedicalRecordCreateView.as_view(), name='patient_home'),
    path('accounts/login/', PatientLoginView.as_view(), name='patient_login'),
    path('accounts/signup/', PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/p/login/', DoctorLoginView.as_view(), name='practitioner_login'),
    path('accounts/p/signup/', DoctorSignupView.as_view(), name='practitioner_signup'),
    path('accounts/p/logout/', DoctorLogoutView.as_view(), name='practitioner_logout'),
]

