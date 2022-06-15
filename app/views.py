from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClientSerializers,DeviceSerializers
from .models import Client,Device
# Create your views here.

class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

class DeviceView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializers



