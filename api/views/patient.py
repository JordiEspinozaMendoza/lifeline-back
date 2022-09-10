from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.patient import PatientSerializer
from api.models import Patient


class PatientView(APIView):
    def get(self, request):
        try:
            items = Patient.objects.all()
            serializer = PatientSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            item = Patient.objects.create(
                name=data["name"],
                lastName=data["lastName"],
                age=data["age"],
                disease=data["disease"],
            )
            item.save()
            return Response({"message": "Item created successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PatientDetails(APIView):
    def get(self, request, pk):
        try:
            item = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            data = request.data
            item = Patient.objects.get(pk=pk)
            item.name = data["name"]
            item.lastName = data["lastName"]
            item.age = data["age"]
            item.disease = data["disease"]
            item.save()
            return Response({"message": "Item modified successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
