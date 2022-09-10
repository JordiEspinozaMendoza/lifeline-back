from rest_framework import serializers
from api.serializers.ambulance import AmbulanceSerializer
from api.serializers.driver import DriverSerializer
from api.models import AmbulanceDriver, Ambulance, Driver

class AmbulanceDriverSerializer(serializers.ModelSerializer):
    ambulance = serializers.SerializerMethodField(
        read_only=True
    )
    driver = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = AmbulanceDriver
        fields = '__all__'

    def get_ambulance(self, obj):
        ambulance = Ambulance.objects.filter(_id=obj.ambulance._id)
        if ambulance.exists():
            return AmbulanceSerializer(ambulance, many=True).data
        return None
    
    def get_driver(self, obj):
        driver = Driver.objects.filter(driver__pk=obj.driver._id)
        if driver.exists():
            return DriverSerializer(driver, many=True).data
        return None
