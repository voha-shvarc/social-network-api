from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from utils import BaseViewSet
from .serializers import PostCreationSerializer, LikeCreationSerializer, LikesAnalyticRetrieveSerializer
from .models import Like
from .services import LikesAnalyticService


class PostViewSet(CreateModelMixin, BaseViewSet):
    action_serializers = {
        "create": PostCreationSerializer,
        "like": LikeCreationSerializer
    }
    permission_classes = (IsAuthenticated,)

    @action(methods=("post",), detail=True, url_path="like", url_name="like")
    def like(self, request, pk=None):
        serializer = self.get_serializer(data={"post": pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status.HTTP_200_OK)

    @action(methods=("delete",), detail=True, url_path="unlike", url_name="unlike")
    def unlike(self, request, pk=None):
        if Like.objects.filter(user=request.user, post=pk).exists():
            Like.objects.filter(user=request.user, post=pk).delete()
            return Response({}, status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You don't have a like on this post yet"}, status.HTTP_400_BAD_REQUEST)


class LikeViewSet(BaseViewSet):
    action_serializers = {
        "analytics": LikesAnalyticRetrieveSerializer
    }

    @action(methods=("get",), detail=False, url_path="analytics", url_name="analytics")
    def analytics(self, request, *args, **kwargs):
        date_from, date_to = request.GET.get("date_from"), request.GET.get("date_to")
        if date_from is None or date_to is None:
            return Response({"error": "'date_from' and 'date_to' are required query parameters"},
                            status.HTTP_400_BAD_REQUEST)

        analytics = LikesAnalyticService.get_total_likes_by_day(date_from, date_to)

        serializer = self.get_serializer(data=analytics, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status.HTTP_200_OK)
