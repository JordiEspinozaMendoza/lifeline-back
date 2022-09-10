from rest_framework import serializers
from api.models import Driver, AmbulanceDriver
import api.serializers.ambulance as a

class DriverSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Driver
        fields = '__all__'


class DriverNoDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'