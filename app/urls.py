from django.urls import path, include
from .views import ClientView, DeviceView, ManufacturerView, ModelView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', ClientView)
router.register(r'device', DeviceView)
router.register(r'manufacturer', ManufacturerView)
router.register(r'model', ModelView)
urlpatterns = router.urls
