
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('blood.urls',)),
    path('',include('donor.urls',)),
    path('',include('patient.urls',)),
    path('', include('registrations.urls')),


]
