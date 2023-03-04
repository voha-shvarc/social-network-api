from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    action_serializers = {}

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)
