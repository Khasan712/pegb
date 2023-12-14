from rest_framework import serializers
from v1.models.users import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if not user.is_staff and not user.is_email_verified:
            raise ValidationError("You have to varify your email")
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 're_password')
    
        extra_kwargs = {
            "re_password": {"write_only": True},
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        super().validate(attrs)
        password = attrs.get('password')
        re_password = attrs.pop('re_password')
        if password != re_password:
            raise serializers.ValidationError(
                {
                    "error": 'The two passwords are different.',
                }
            )
        attrs['password'] = make_password(password)
        attrs['customer_category'] = 'bronze'
        return attrs


class StaffRegisterSerializer(UserRegisterSerializer):

    def create(self, validated_data):
        validated_data['is_staff'] = True
        validated_data['is_email_verified'] = True
        return super().create(validated_data)
