from django.urls import path
from pages.views.general import StatPageView, HomePageView
from pages.views.patients import PatientSignUpView, PatientLoginView, MedicalRecordCreateView
from pages.views.practitioner import (
    DoctorLoginView as practitioner_login_page,
    logout_page as practitioner_logout_page,
    signup_page as practitioner_signup_page,
    show_doc_info
)

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('stat/', StatPageView.as_view(), name='stat_page'),
    path('report/', MedicalRecordCreateView.as_view(), name='patient_home'),
    path('dashboard/', show_doc_info, name='practitioner_home'),
    path('accounts/login/', PatientLoginView.as_view(), name='patient_login'),
    path('accounts/signup/', PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/p/logout/', practitioner_logout_page, name='practitioner_logout'),
]

