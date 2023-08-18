from rest_framework import viewsets
from rest_framework import permissions

from django.http import HttpResponse

from wallpaper.models import Image
from wallpaper.serializers import ImageSerializer

class ImageViewset(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    
def test_view(request):
    return HttpResponse("200 OK")