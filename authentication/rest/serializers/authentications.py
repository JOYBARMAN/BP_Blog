"""Serializer for authentication"""

from django.contrib.auth import authenticate
from django.core.validators import MinValueValidator, MaxValueValidator

from rest_framework import serializers

from core.models import User, UserOtp
from core.choices import OtpType
from core.utils import is_valid_bd_phone_num, send_otp_to_user
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
        send_otp_to_user(user=user, otp_type=OtpType.REGISTRATION)
        return {
            "message": "Registration Successful. OTP send to your mail please activate your account.",
            "token": token,
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(style={"input_type": "password"}, required=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user)
            return {"msg": "Login Successful", "token": token}
        else:
            raise serializers.ValidationError(
                {"non_field_errors": "Email or Password is not valid"}
            )


class ActivateAccountSerializer(serializers.ModelSerializer):
    otp = serializers.IntegerField()

    class Meta:
        model = UserOtp
        fields = ["otp"]

    def create(self, validated_data):
        request = self.context["request"]
        user_otp = UserOtp.objects.get(user=request.user)

        if validated_data["otp"] != user_otp.otp:
            raise serializers.ValidationError({"otp": "Invalid OTP."})
        elif user_otp.is_expired():
            raise serializers.ValidationError({"otp": "OTP Expired."})
        else:
            user_otp.is_activated = True
            user_otp.save()

            return {"message": "Your account has been successfully activated."}
