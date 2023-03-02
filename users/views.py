from django.contrib.auth.models import update_last_login
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from .serializers import UserSignUpSerializer, UserSignInSerializer, JwtTokenRetrieveSerializer
from .services import AuthUserService


class UserAuthViewSet(GenericViewSet):
    action_serializers = {
        "sign_up": UserSignUpSerializer,
        "sign_in": UserSignInSerializer
    }

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    @action(methods=("post",), detail=False, url_path="sign-up", url_name="sign-up")
    def sign_up(self, request: Request, *args, **kwargs):
        serializer: UserSignUpSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({}, status=HTTP_201_CREATED)

    @action(methods=("post",), detail=False, url_path="sign-in", url_name="sign-up")
    def sign_in(self, request: Request, *args, **kwargs):
        serializer: UserSignInSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get("user")
        update_last_login(None, user)
        tokens_data = AuthUserService.generate_tokens(user)
        response_data = JwtTokenRetrieveSerializer(tokens_data).data

        return Response(response_data, HTTP_200_OK)
