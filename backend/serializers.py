from .models import DoctorDetails,PatientDetails,Records,Chat
from rest_framework import serializers

class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetails
        fields = '__all__'

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
