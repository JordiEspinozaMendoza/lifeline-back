from rest_framework import serializers
from api.models import AmbulanceDriver, Ambulance, Driver
import api.serializers.ambulancedriver as ad
import api.serializers.driver as d

class AmbulanceSerializer(serializers.ModelSerializer):
    drivers = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Ambulance
        fields = '__all__'

    def get_drivers(self, obj):
        driver = AmbulanceDriver.objects.filter(ambulance=obj._id)
        if driver.exists():
            return ad.AmbulanceDriverDetailsSerializer(driver, many=True).data
        return None

class AmbulanceNoDetailsSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Ambulance
        fields = '__all__'
    
    def get_driver(self, obj):
        driver = AmbulanceDriver.objects.filter(ambulance=obj._id)
        drivers = Driver.objects.filter(pk__in=driver.values('driver'))
        if driver.exists():
            return d.DriverSerializer(drivers, many=True).data
        return None

class AmbulanceSerializerNoDriver(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = '__all__'