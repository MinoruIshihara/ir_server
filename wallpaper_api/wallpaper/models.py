from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from rest_framework.authtoken.models import Token

import uuid

from config import settings


def upload_to(instance, filename):
    return "wallpaper/{filename}".format(filename=filename)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to=upload_to, null=True, blank=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and instance is not None:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_dields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_dields)
        user.set_password(password)
        user.save(using=self.db)
        user.full_clean()

        Token.objects.create(user=user)

        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_supervisor", False)

        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_supervisor", True)

        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)

    email = models.EmailField(unique=True)

    is_supervisor = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"name: {self.username}, email: {self.email}, supervisor: {self.is_supervisor}, active: {self.is_active}"

    class Meta:
        db_table = "wallpaper_user"
