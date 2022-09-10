from rest_framework import serializers
from api.models import Driver, AmbulanceDriver
import api.serializers.ambulance as a

class DriverSerializer(serializers.ModelSerializer):
    ambulance = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Driver
        fields = '__all__'

    def get_ambulance(self, obj):
        ambulance = AmbulanceDriver.objects.filter(driver_id=obj._id)
        if ambulance.exists():
            return a.AmbulanceSerializer(ambulance, many=True).data
        return None
