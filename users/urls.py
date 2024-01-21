from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserAuthViewSet, UserViewSet

router = DefaultRouter()
router.register("", UserAuthViewSet, basename="users-auth")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("sign-in/", TokenObtainPairView.as_view(), name="sign-in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

urlpatterns += router.urls
