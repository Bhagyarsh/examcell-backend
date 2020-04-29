# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.settings import api_settings
import datetime
from django.utils import timezone
from rest_framework.views import exception_handler
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# payload = jwt_payload_handler(user)
# token = jwt_encode_handler(payload)


expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserRegisterSerializer(serializers.ModelSerializer):
    expires = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    # password2 = serializers.CharField(
    #     style={'input_type':'password'},
    #     write_only=True
    # )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password', 'token', 'expires',)
        extra_kwargs = {'password': {'write_only': True}}

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    
    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def create(self, validated_data):
        new_user = User.objects.create_user(
            username=validated_data.get("username"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            password=validated_data.get("password"))
        return new_user




class UserUpdateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'password', 'token', 'expires')
        extra_kwargs = {'password': {'write_only': True}}
