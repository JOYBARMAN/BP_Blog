"""Serializers for admin site add and update users"""

from rest_framework import serializers

from core.models import User
from core.utils import is_valid_bd_phone_num


class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
    )
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "uid",
            "username",
            "phone",
            "email",
            "password",
            "confirm_password",
            "is_active",
            "is_admin",
            "user_type",
            "status",
        ]
        read_only_fields = ["id", "uid"]

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
        password, confirm_password = validated_data.pop(
            "password", None
        ), validated_data.pop("confirm_password", None)

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
