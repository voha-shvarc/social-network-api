from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from utils import BaseViewSet
from .serializers import UserSignUpSerializer, UserActivityRetrieveSerializer
from .models import User


class UserAuthViewSet(BaseViewSet):
    action_serializers = {
        "sign_up": UserSignUpSerializer,
    }

    @action(methods=("post",), detail=False, url_path="sign-up", url_name="sign-up")
    def sign_up(self, request: Request, *args, **kwargs):
        serializer: UserSignUpSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({}, status=status.HTTP_201_CREATED)


class UserViewSet(BaseViewSet):
    action_serializers = {
        "activity": UserActivityRetrieveSerializer,
    }

    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    @action(methods=("get",), detail=True, url_path="activity", url_name="activity")
    def activity(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)

        return Response(serializer.data, status.HTTP_200_OK)
