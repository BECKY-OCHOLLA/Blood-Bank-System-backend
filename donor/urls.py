from django.urls import path
from . import views



urlpatterns = [
    path('api/donor/', views.DonorList.as_view()),
    path('api/donate/', views.BloodDonateList.as_view())
]
