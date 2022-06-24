from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializers
from .models import CustomUser

from rest_framework import permissions


from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.author == request.user:
    #         return True
    #     return False


class UsersViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AuthorOrReadOnly]
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
