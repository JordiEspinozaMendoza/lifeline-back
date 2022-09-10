from rest_framework import serializers
from api.models import AmbulanceDriver, Ambulance, Driver
import api.serializers.driver as d

class AmbulanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ambulance
        fields = '__all__'

class AmbulanceNoDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ambulance
        fields = '__all__'