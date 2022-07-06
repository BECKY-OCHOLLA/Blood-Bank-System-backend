from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import DoctorSignupView, DonorSignupView, PatientSignupView, LoginView, UserView, LogoutView

urlpatterns = [
    path('', views.getRoutes),
    path('api/signup/doctor', DoctorSignupView.as_view()),
    path('api/signup/donor', DonorSignupView.as_view()),
    path('api/signup/patient', PatientSignupView.as_view()),
    path('api/login', LoginView.as_view()),
    path('api/user', UserView.as_view()),
    path('api/logout', LogoutView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
