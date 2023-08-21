from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from wallpaper.views import ImageViewset
from wallpaper.views import test_view

router = routers.DefaultRouter()
router.register(r"image", ImageViewset, basename="image")

urlpatterns = [
    path("", include(router.urls)),
    path("test", test_view),
    path("controll", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

