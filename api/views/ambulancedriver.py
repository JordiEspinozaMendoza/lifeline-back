from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.ambulancedriver import AmbulanceDriverSerializer
from api.models import AmbulanceDriver


class AmbulanceDriverView(APIView):
    def get(self, request):
        try:
            items = AmbulanceDriver.objects.all()
            serializer = AmbulanceDriverSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            item = AmbulanceDriver.objects.create(
                ambulance_id=data["ambulance"],
                driver_id=data["driver"],
            )
            item.save()
            return Response({"message": "Item created successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceDriverDetails(APIView):
    def get(self, request, pk):
        try:
            item = AmbulanceDriver.objects.get(pk=pk)
            serializer = AmbulanceDriverSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = request.data
            item = AmbulanceDriver.objects.get(pk=pk)
            item.ambulance_id = data["ambulance"]
            item.driver_id = data["driver"]
            item.save()
            return Response({"message": "Item modified successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
