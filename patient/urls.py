from django.urls import path
from . import views


urlpatterns = [
    path('api/patient/', views.PatientList.as_view())
]