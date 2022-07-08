
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('blood.urls',)),
    path('',include('donor.urls',)),
    path('',include('patient.urls',)),
    path('', include('registrations.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name="index")


]
