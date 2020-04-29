# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.settings import api_settings
import datetime
from accounts.models import profile
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
    dp = serializers.ImageField(required=False, max_length=None,
                                allow_empty_file=True, use_url=True)
    parents = serializers.BooleanField(default=False)
    student = serializers.BooleanField(default=True)
    staff = serializers.BooleanField(default=False)
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
                  'password', 'token', 'expires', "dp", "parents", "student", "staff")
        extra_kwargs = {'password': {'write_only': True}, 'dp': {'write_only': True, 'required': False, 'allow_null': True},
                        'parents': {'write_only': True}, 'student': {'write_only': True}, 'staff': {'write_only': True}}

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)


    def create(self, validated_data):
        print("===============================")
        print(validated_data)
        new_user = User.objects.create_user(
            username=validated_data.get("username"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            password=validated_data.get("password"))

        updateprofile = profile.objects.create(
            user=new_user, dp=validated_data["dp"], college_staff=validated_data["staff"],
            student=validated_data["student"],parents=validated_data["parents"])

        return new_user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        attrs['user'] = self.context['request'].user


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
