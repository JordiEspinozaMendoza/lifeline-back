from django.urls import path
from api.views import driver

urlpatterns = [
    path('', driver.DriverView.as_view(), name="Driver View"),
    path('<int:pk>/', driver.DriverDetails.as_view(), name="Driver Details"),
]
