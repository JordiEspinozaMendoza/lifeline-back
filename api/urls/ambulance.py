from django.urls import path
from api.views.ambulance import AmbulanceView, AmbulanceDetails

urlpatterns = [
    path('', AmbulanceView.as_view(), name="Ambulance View"),
    path('<int:pk>/', AmbulanceDetails.as_view(), name="Ambulance Details"),
]