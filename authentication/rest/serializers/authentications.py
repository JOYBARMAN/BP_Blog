"""Serializer for authentication"""

from rest_framework import serializers

from core.models import User
from core.utils import is_valid_bd_phone_num


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
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

        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )

        if value != confirm_password:
            raise serializers.ValidationError(
                "password and confirm password do not match."
            )

        return value

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        return User.objects.create_user(**validated_data)
