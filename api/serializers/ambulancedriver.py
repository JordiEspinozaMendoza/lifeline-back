from rest_framework import serializers
import api.serializers.ambulance as a
from api.serializers.driver import DriverNoDetailsSerializer, DriverSerializer
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
        fields = "__all__"

    def get_ambulance(self, obj):
        if obj.ambulance:
            return a.AmbulanceNoDetailsSerializer(obj.ambulance, many=False).data
        return None
    
    def get_driver(self, obj):
        getDrivers = Driver.objects.filter(_id=obj.driver_id)
        if getDrivers.exists():
            return DriverNoDetailsSerializer(getDrivers, many=True).data
        return None

class AmbulanceDriverDetailsSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = AmbulanceDriver
        fields = ('driver',)

    def get_driver(self, obj):
        if obj.driver:
            return DriverSerializer(obj.driver, many=False).data
        return None
