from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'first_name', 'phone', 'email','role', 'password']
        extra_kwargs = {'password': {'write_only': True}}
