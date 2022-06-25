from django.urls import path, include
from .views import UsersViewSet, UserList
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'', UsersViewSet)
urlpatterns = [
    path('u', UserList.as_view()),
    path('', UsersViewSet.as_view(), name='home')
]


