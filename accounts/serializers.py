
from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class SendOTPSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=15)
    def validate_phone_number(self, value):
        if not value.isdigit() or not value.startswith("09"):
            raise serializers.ValidationError("Phone number must be valid and start with 09.")
        return value



class VerifyOTPSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("کد باید 6 رقمی و عددی باشد.")
        return value





class SwaggerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError("نام کاربری یا رمز عبور اشتباه است.")