from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import PostCreationSerializer


class PostViewSet(CreateModelMixin, GenericViewSet):
    action_serializers = {
        "create": PostCreationSerializer,
    }
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)

