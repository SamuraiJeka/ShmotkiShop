from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.routers.user_router import UserApiView


router = routers.DefaultRouter()
router.register(r'api/users', UserApiView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
