from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.ambulance import AmbulanceSerializer
from api.models import Ambulance


class AmbulanceView(APIView):
    def get(self, request):
        try:
            items = Ambulance.objects.all()
            serializer = AmbulanceSerializer(items, many=True)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            item = Ambulance.objects.create(
                plate=data["plate"],
            )
            item.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceDetails(APIView):
    def get(self, request, pk):
        try:
            item = Ambulance.objects.get(pk=pk)
            serializer = AmbulanceSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = request.data
            item = Ambulance.objects.get(pk=pk)
            item.plate = data["plate"]
            item.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
