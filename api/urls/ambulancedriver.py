from django.urls import path
from api.views import ambulancedriver

urlpatterns = [
    path('', ambulancedriver.AmbulanceDriverView.as_view(), name="AmbulanceDriver View"),
    path('<int:pk>/', ambulancedriver.AmbulanceDriverDetails.as_view(), name="AmbulanceDriver Details"),
]
