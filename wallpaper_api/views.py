from rest_framework import viewsets
from rest_framework import permissions

from models import Image
from serializers import ImageSerializer

class ImageViewset(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()