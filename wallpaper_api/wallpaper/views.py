import re

from django.http import HttpResponse

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from wallpaper.models import Image
from wallpaper.serializers import ImageSerializer
    
def test_view(request):
    return HttpResponse("200 OK")

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def create(self, request):
        file_data = request.data

        serializer = self.get_serializer(data=file_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)