from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.Serializer):
        temp = serializers.DecimalField(max_digits=10, decimal_places=2)
        time_update = serializers.DateTimeField()

class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ["id", 'name', 'description']

"""class SensorSerializerDetail(serializers.ModelSerializer):

    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", 'name', 'description', 'measurements']"""

class SensorSerializerDetail(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    meas = MeasurementSerializer(many=True)







