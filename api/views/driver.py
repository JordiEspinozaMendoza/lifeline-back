from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.driver import DriverNoDetailsSerializer, DriverSerializer
from api.models import Driver


class DriverView(APIView):
    def get(self, request):
        try:
            items = Driver.objects.all()
            serializer = DriverNoDetailsSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            item = Driver.objects.create(
                name=data["name"],
                lastName=data["lastName"],
                phone=data["phone"],
            )
            item.save()
            return Response({"message": "Item created successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DriverDetails(APIView):
    def get(self, request, pk):
        try:
            item = Driver.objects.get(pk=pk)
            serializer = DriverNoDetailsSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = request.data
            item = Driver.objects.get(pk=pk)
            item.name = data["name"]
            item.lastName = data["lastName"]
            item.phone = data["phone"]
            item.save()
            return Response({"message": "Item modified successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
