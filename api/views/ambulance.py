from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.ambulance import AmbulanceNoDetailsSerializer, AmbulanceSerializer
from api.models import Ambulance


class AmbulanceView(APIView):
    def get(self, request):
        try:
            items = Ambulance.objects.all()
            serializer = AmbulanceNoDetailsSerializer(items, many=True)
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
            return Response({"message": "Item created successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AmbulanceDetails(APIView):
    def get(self, request, pk):
        try:
            item = Ambulance.objects.get(pk=pk)
            serializer = AmbulanceNoDetailsSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = request.data
            item = Ambulance.objects.get(pk=pk)
            item.plate = data["plate"]
            item.save()
            return Response({"message": "Item updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
