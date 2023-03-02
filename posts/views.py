from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostCreationSerializer, LikeCreationSerializer
from .models import Like


class PostViewSet(CreateModelMixin, GenericViewSet):
    action_serializers = {
        "create": PostCreationSerializer,
        "like_unlike": LikeCreationSerializer
    }
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

    @action(methods=("post", "delete"), detail=True, url_path="likes", url_name="likes")
    def like_unlike(self, request, pk=None):
        if request.method == "POST":
            serializer = self.get_serializer(data={"post": pk})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        # delete
        if Like.objects.filter(user=request.user, post=pk).exists():
            Like.objects.filter(user=request.user, post=pk).delete()
            return Response({}, status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You don't have like on this post yet"}, status.HTTP_400_BAD_REQUEST)
