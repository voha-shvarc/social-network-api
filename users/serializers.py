from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import Serializer, ModelSerializer, EmailField, CharField, ValidationError

from .models import User


class UserSignUpSerializer(ModelSerializer):
    email = EmailField()
    password = CharField()

    @staticmethod
    def validate_password(value):
        validate_password(value)
        return make_password(value)

    @staticmethod
    def validate_email(value):
        email = User.objects.normalize_email(value)
        if User.objects.filter(email=email).exists():
            raise ValidationError({"error": "User with this email already exists"})
        return email

    class Meta:
        model = User
        fields = ("email", "password")


class UserSignInSerializer(ModelSerializer):
    email = EmailField()
    password = CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = get_object_or_404(self.Meta.model, email=email)

        if not user.check_password(password):
            print(f"Password {password} is not correct")

            raise ValidationError({"error": "Wrong password"})

        attrs["user"] = user
        return attrs

    class Meta:
        model = User
        fields = ("email", "password")

class JwtTokenRetrieveSerializer(Serializer):
    access_token = CharField()
    refresh_token = CharField()

    class Meta:
        fields = ("access_token", "refresh_token")
        read_only_fields = fields
