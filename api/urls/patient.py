from django.urls import path
from api.views import patient

urlpatterns = [
    path('', patient.PatientView.as_view(), name="Driver View"),
    path('<int:pk>/', patient.PatientDetails.as_view(), name="Driver Details"),
]
