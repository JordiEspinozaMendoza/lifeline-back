from rest_framework import serializers
from api.serializers.ambulance import AmbulanceNoDetailsSerializer, AmbulanceSerializer
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
        print(AmbulanceSerializer(obj.ambulance))
        if obj.ambulance:
            return AmbulanceNoDetailsSerializer(obj.ambulance, many=False).data
        return None
    
    def get_driver(self, obj):
        getDrivers = Driver.objects.filter(_id=obj.driver_id)
        if getDrivers.exists():
            return DriverNoDetailsSerializer(getDrivers, many=True).data
        return None
