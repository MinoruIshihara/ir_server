from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from wallpaper.views import test_view

urlpatterns = [
    path("", test_view),
    path("controll", admin.site.urls),
    path("wallpaper/", include("wallpaper.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

