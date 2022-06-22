from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializers
from .models import CustomUser


# Create your views here.

class UsersViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
