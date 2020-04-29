# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from notice.models import notice

from notice.models import notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = notice
        fields = '__all__'

        