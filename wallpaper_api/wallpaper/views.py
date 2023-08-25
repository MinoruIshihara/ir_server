import os

from django.http import HttpResponse, FileResponse

from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import get_object_or_404

from config.settings import MEDIA_ROOT

from wallpaper.models import Image
from wallpaper.serializers import ImageSerializer
    
def test_view(request):
    return HttpResponse("200 OK", HTTP_200_OK)

class ImageViewset(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def create(self, request):
        file_data = request.data

        serializer = self.get_serializer(data=file_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

class ImageDownloadVIew(GenericViewSet, ListModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def list(self, request, image_pk=None):
        iamge_path = get_object_or_404(self.queryset, pk=image_pk)
        selializer = self.get_serializer(iamge_path)
        _, file_name = os.path.split(selializer.data["file"])
        image_path = os.path.join(MEDIA_ROOT, file_name)
        image_name = selializer.data["name"]
        
        return FileResponse(open(image_path, "rb"), as_attachment=True, filename=image_name)
    