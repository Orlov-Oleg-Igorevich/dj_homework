# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import io
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorSerializerDetail


class TempView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self , request):
        data_json = request.data
        rq = Sensor.objects.create(**data_json)
        return Response({'status': rq.name})

class SensorViewDetails(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializerDetail

    def patch(self, request, pk):
        rq = Sensor.objects.filter(id=pk).update(**request.data)
        print(rq)
        return Response({'status': rq})

    def post(self, request):
        data_json = request.data
        rq = Measurement.objects.create(sensor_id = data_json.get('sensor'), temp = data_json.get('temperature'))
        return Response({'status': rq.sensor_id})