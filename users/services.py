from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class AuthUserService:
    @staticmethod
    def generate_tokens(user: User):
        refresh: RefreshToken = RefreshToken.for_user(user)

        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }
