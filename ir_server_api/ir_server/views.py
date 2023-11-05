import logging
import os
from datetime import datetime, timedelta

from config.settings import EMAIL_SENDER, EXPIRED_DAYS, HOST_NAME, MEDIA_ROOT
from django.core.mail import send_mail
from django.http import FileResponse, HttpResponse
from ir_server.models import Image, User, UserActivationToken
from ir_server.serializers import (
    ImageSerializer,
    UserActivationTokenSerializer,
    UserSerializer,
)
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet, ModelViewSet


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

    def retrieve(self, request, pk=None):
        if pk == "latest":
            objs = self.get_queryset().all()
            latest_id = objs.latest("created_at").id
            latest_obj = get_object_or_404(objs, pk=latest_id)
            serializer = self.get_serializer(latest_obj)
            return Response(data=serializer.data)
        else:
            return super().retrieve(self, request, pk)


class ImageDownloadView(GenericViewSet, ListModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def list(self, request, image_pk=None):
        iamge_path = get_object_or_404(self.queryset, pk=image_pk)
        selializer = self.get_serializer(iamge_path)
        _, file_name = os.path.split(selializer.data["file"])
        image_path = os.path.join(MEDIA_ROOT, "ir_server", file_name)
        image_name = selializer.data["name"]

        return FileResponse(
            open(image_path, "rb"), as_attachment=True, filename=image_name
        )


class CreateUserViewSet(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def _send_activation_email(self, user: User):
        logger = logging.getLogger("ir-server-api")
        expired_at = datetime.now() + timedelta(EXPIRED_DAYS)
        user_id = user.id
        serializer = UserActivationTokenSerializer(
            data={"user_id": user_id, "expired_at": expired_at}
        )
        serializer.is_valid(raise_exception=True)
        user_activation_token = serializer.save()
        user_email = user.email
        token = user_activation_token.token
        subject = "アカウント認証のお願い"
        message = f"以下のリンクをクリックしてメールアドレスの認証を行ってください\n {HOST_NAME}/{token}/activate"
        send_mail(
            from_email=EMAIL_SENDER,
            recipient_list=[user_email],
            subject=subject,
            message=message,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        self._send_activation_email(user)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
