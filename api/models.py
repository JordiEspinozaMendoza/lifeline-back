from django.db import models

# Create your models here.
class Ambulance(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    plate = models.CharField(max_length=10)


class Driver(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)


class AmbulanceDriver(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, default="6640000000")


class Patient(models.Model):
    name = models.CharField(max_length=75)
    lastName = models.CharField(max_length=75)
    age = models.IntegerField()
    disease = models.CharField(max_length=75, default="")
