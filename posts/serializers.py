from rest_framework import serializers

from .models import Post, Like


class PostCreationSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = ("title", "text", "user")
        model = Post


class LikeCreationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        post_id = attrs.get("post")
        if Like.objects.filter(user=self.context["request"].user, post=post_id).exists():
            raise serializers.ValidationError({"error": "You've already liked this post"})

        return attrs

    class Meta:
        fields = ("user", "post", "date_added")
        model = Like
