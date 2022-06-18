from rest_framework import serializers

from .models import Client, Device, Model, Manufacturer


class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class ManufacturerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class DeviceSerializers(serializers.ModelSerializer):
    model = ModelSerializers()
    manufacturer = ManufacturerSerializers()

    class Meta:
        model = Device
        fields = '__all__'


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
