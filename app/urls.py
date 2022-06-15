from django.urls import path
from .views import ClientView,DeviceView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('client/', ClientView.as_view(), name='client'),
    path('device/', DeviceView.as_view(), name='device')

]