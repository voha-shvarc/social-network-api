from rest_framework import serializers

from .models import Post, Like


class PostCreationSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = ("title", "text", "user")
        model = Post

