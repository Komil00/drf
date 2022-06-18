from django.urls import path, include
from .viewsets import ClientView, DeviceView, ManufacturerView, ModelView, BaseView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', BaseView)
router.register(r'client', ClientView)
router.register(r'device', DeviceView)
router.register(r'manufacturer', ManufacturerView)
router.register(r'model', ModelView)
urlpatterns = router.urls
