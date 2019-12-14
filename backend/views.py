from django.shortcuts import render
import json
# from .models import Election, Constituency, AadharDetail, ElectionConstituency, Party, PartyCandidate
# from .serializers import ElectionSerializer, ConstituencySerializer, AadharDetailSerializer, ElectionConstituencySerializer, PartySerializer, PartyCandidateSerializer
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
    