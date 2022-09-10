from rest_framework import serializers
from api.models import AmbulanceDriver, Ambulance
import api.serializers.driver as d

class AmbulanceSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Ambulance
        fields = '__all__'

    def get_driver(self, obj):
        driver = AmbulanceDriver.objects.filter(ambulance_id=obj._id)
        if driver.exists():
            return d.DriverSerializer(driver, many=True).data
        return None
