from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .serializers import ClientSerializers, DeviceSerializers, ModelSerializers, ManufacturerSerializers
from .models import Client, Device, Model, Manufacturer, Loan, LoadPayment


# Create your views here.

class ClientView(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializers(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class DeviceView(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializers


class ModelView(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Model.objects.all()
    serializer_class = ClientSerializers

    def list(self, request):
        queryset = Model.objects.all()
        serializer = ModelSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=True):
        queryset = Model.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ModelSerializers(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ModelSerializers(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class ManufacturerView(ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializers

    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ManufacturerSerializers(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
