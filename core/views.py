from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializers, UserSerializer
from .models import CustomUser

from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        """
        Return True if permission is granted, False otherwise.
        """
        return bool(request.user and request.user.is_authenticated)

    # def has_object_permission(self, request, view, obj):
    #     """
    #     Return True if permission is granted, False otherwise.
    #     """
    #     return bool(
    #         request.method in SAFE_METHODS or
    #         obj.author == request.user
    #     )


class UsersViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers


# class UserView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_update(self, serializer):
#         if self.request.user.is_staff:
#             instance = self.get_object()
#             serializer.save(instance=instance)
#         if self.request.user.role == 'MANAGER':
#             user = CustomUser.objects.get(pk=self.kwargs['pk'])
#             if user.role == 'OPERATOR':
#                 instance = self.get_object()
#                 serializer.save(instance=instance)
#             else:
#                 return None

