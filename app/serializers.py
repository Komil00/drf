from rest_framework import serializers

from .models import Client, Device
from core.models import CustomUser


class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class ClientSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=CustomUser.objects.all(), slug_field='username')
    class Meta:
        model = Client
        fields = '__all__'

