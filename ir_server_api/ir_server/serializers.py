import logging
from typing import Any, Dict

from ir_server.models import Image, Stat, User, UserActivationToken
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "name", "created_at", "file"]


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ["id", "name", "created_at", "file"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserActivationTokenSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = UserActivationToken
        fields = ["user_id", "expired_at"]

    def create(self, validated_data: Dict[str, Any]) -> UserActivationToken:
        logger = logging.getLogger("ir-server-api")
        user_id = validated_data.get("user_id", None)

        if user_id is not None:
            validated_data["user"] = user_id
            del validated_data["user_id"]
        logger.error(validated_data["user"].id)

        return super().create(validated_data)
