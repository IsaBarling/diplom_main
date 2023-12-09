from django.urls import path
from pages.views.general import StatPageView, HomePageView
from pages.views.patients import (
    show_login as patient_show_login,
    show_signup as patient_show_signup,
    show_logout as patient_show_logout,
    patient_create_view
)
from pages.views.practitioner import (
    login_page as practitioner_login_page,
    logout_page as practitioner_logout_page,
    signup_page as practitioner_signup_page,
    show_doc_info
)

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('stat/', StatPageView.as_view(), name='stat_page'),
    path('report/', patient_create_view, name='patient_home'),
    path('dashboard/', show_doc_info, name='practitioner_home'),
    path('accounts/login/', patient_show_login, name='patient_login'),
    path('accounts/signup/', patient_show_signup, name='patient_signup'),
    path('accounts/logout/', patient_show_logout, name='patient_logout'),
    path('accounts/p/login/', practitioner_login_page, name='practitioner_login'),
    path('accounts/p/signup/', practitioner_signup_page, name='practitioner_signup'),
    path('accounts/p/logout/', practitioner_logout_page, name='practitioner_logout'),
]

