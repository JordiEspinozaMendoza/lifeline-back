from rest_framework import serializers
from api.models import AmbulanceDriver, Ambulance, Driver
import api.serializers.ambulancedriver as ad

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

    class Meta:
        model = Ambulance
        fields = '__all__'