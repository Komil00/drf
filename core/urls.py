from django.urls import path, include
from .views import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UsersViewSet)
urlpatterns = router.urls
