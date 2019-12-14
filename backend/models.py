from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DoctorDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_num = models.CharField(max_length=20)
    aadhar_num = models.CharField(max_length=20)
    finger_print = models.TextField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField(max_length=255)
    pincode = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name 

class PatientDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_num = models.CharField(max_length=20)
    aadhar_num = models.CharField(max_length=20)
    finger_print = models.TextField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField(max_length=255)
    pincode = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name 

class Records(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor_id = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    timeStamp = models.IntegerField()
    date = models.DateField()
    summary = models.TextField(max_length=2550)

class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor_id = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    timeStamp = models.IntegerField()
    date = models.DateField()
    doctors_message = models.TextField(max_length=255)
    patient_message = models.TextField(max_length=255)
    timestamp_message  = models.IntegerField()
    def __str__(self):
        return self.id
