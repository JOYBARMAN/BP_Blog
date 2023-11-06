"""Serializer for authentication"""

from django.contrib.auth import authenticate
from rest_framework import serializers

from core.models import User
from core.utils import is_valid_bd_phone_num
from authentication.utils import get_tokens_for_user


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, min_length=8, required=True
    )
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, min_length=8, required=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "phone",
            "email",
            "user_type",
            "password",
            "confirm_password",
        ]

    def validate_phone(self, value):
        if value and not is_valid_bd_phone_num(value):
            raise serializers.ValidationError(
                "This is not a valid Bangladeshi phone number "
            )
        return value

    def validate_password(self, value):
        confirm_password = self.initial_data.get("confirm_password", "")

        if value != confirm_password:
            raise serializers.ValidationError(
                "password and confirm password do not match."
            )

        return value

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        user = User.objects.create_user(**validated_data)
        token = get_tokens_for_user(user)
        return {"msg": "Registration Successful", "token": token}


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = authenticate(username=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            return {"msg": "Login Successful", "token": token}
        else:
            raise serializers.ValidationError(
                {"non_field_errors": "Email or Password is not valid"}
            )
