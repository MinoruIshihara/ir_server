from django.urls import include, path
from ir_server.views import CreateUserViewSet, ImageDownloadView, ImageViewset, StatView
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r"image", ImageViewset, basename="image")
router.register(r"auth/create", viewset=CreateUserViewSet, basename="auth")

image_router = routers.NestedSimpleRouter(
    router, r"image", lookup="image", trailing_slash=False
)
image_router.register(r"download", ImageDownloadView)

stat_router = routers.NestedSimpleRouter(
    router, r"statistics", lookup="statistics", trailing_slash=False
)
stat_router.register(r"download", StatView)


urlpatterns = [
    path("", include(router.urls)),
    path("", include(image_router.urls)),
    path("", include(stat_router.urls)),
]
