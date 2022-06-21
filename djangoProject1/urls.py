import rest_framework
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('app.urls')),
    path('auth/users/', include('core.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('rest_framework.urls')),
]