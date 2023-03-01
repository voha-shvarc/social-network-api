from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserAuthViewSet

router = DefaultRouter()
router.register("", UserAuthViewSet, basename="users")

urlpatterns = [
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh")
]

urlpatterns += router.urls
