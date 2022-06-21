from django.urls import path, include
from .viewsets import ClientViewSet, DeviceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'', BaseView)
router.register(r'client', ClientViewSet)
router.register(r'device', DeviceViewSet)

urlpatterns = router.urls
