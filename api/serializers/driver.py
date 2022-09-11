from rest_framework import serializers
from api.models import Driver, AmbulanceDriver
import api.serializers.ambulance as a

class DriverSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Driver
        fields = '__all__'


class DriverNoDetailsSerializer(serializers.ModelSerializer):
    ambulance = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Driver
        fields = '__all__'

    def get_ambulance(self, obj):
        driver = AmbulanceDriver.objects.filter(driver=obj._id)
        ambulance = a.Ambulance.objects.filter(pk__in=driver.values('ambulance'))
        if ambulance.exists():
            return a.AmbulanceSerializerNoDriver(ambulance, many=True).data
        return None