from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from views import ImageViewset

router = routers.DefaultRouter()
router.register(r"images", viewset=ImageViewset)

urlpatterns = [
    path("controll", admin.site.urls),
    path("", include(router.urls))
]