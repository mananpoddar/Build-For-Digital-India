from django.shortcuts import render
import json
from .models import DoctorDetails,PatientDetails,Records,Chat
from .serializers import DoctorDetailsSerializer,PatientDetailsSerializer,RecordsSerializer,ChatSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def index(request):
    print("manan")

# Create your views here.
# @csrf_exempt 
class EnterRecordAPI(APIView):

	def post(self, request):
        serializer = Records(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveRecordAPI(APIView):

    def post(self,request):

        try:
            data = json.loads(str(request.body, encoding='utf-8'))
            doctor_id = data["doctor_id"]
            patient_id = data["patient_id"]
            timestamp = data["timestamp"]
            date = data["date"]
            obj = Records.objects.filter(doctor_id=doctor_id,patient_id=patient_id,timestamp=timestamp,date=date)
            return_data = obj.summary
            return_data = json.dumps(return_data)
            return Response(return_data,status=status.HTTP_200_OK)
        except:
            # print("except")
            return Response(status=status.HTTP_204_NO_CONTENT)
    