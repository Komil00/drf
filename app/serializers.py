from rest_framework import serializers

from .models import Client,Device


class DeviceSerializers(serializers.ModelSerializer):
        class Meta:
            model = Device
            fields = '__all__'

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
