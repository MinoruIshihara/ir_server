from django.urls import include, path
from rest_framework_nested import routers

from wallpaper.views import ImageViewset, ImageDownloadVIew

router = routers.SimpleRouter()
router.register(r"image", ImageViewset, basename="image")

image_router = routers.NestedSimpleRouter(router, r"image", lookup="image", trailing_slash=False)
image_router.register(r"download", ImageDownloadVIew)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(image_router.urls)),
]