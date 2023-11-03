from rest_framework import serializers
from ir_server.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "name", "created_at", "file"]