import datetime
import uuid

from config import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def upload_to(instance, filename):
    return "ir_server/{filename}".format(filename=filename)


def save_stat_to(instance, filename):
    return "ir_server/stat/{filename}".format(filename=filename)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to=upload_to, null=True, blank=True)


class Stat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to=save_stat_to, null=True, blank=True)


class UserManager(BaseUserManager):
    def _valid_email(self, email):
        if not email:
            raise ValueError("Email should not be empty")

    def _valid_username(self, username):
        if not username:
            raise ValueError("UserName should not be empty")

    def _create_user(self, email, username, password, **extra_dields):
        self._valid_email(email)
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
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    is_supervisor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def has_module_perms(self, ir_server):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def __str__(self):
        return f"name: {self.username}, email: {self.email}, supervisor: {self.is_supervisor}, active: {self.is_active}"

    class Meta:
        db_table = "users"


class UserActivationTokenManager(models.Manager):
    def activate_user(self, token):
        activation_token = self.filter(token=token, expired_at__gte=datetime.now())
        activation_user = activation_token.user
        activation_user.is_active = True
        activation_user.save()
        return activation_user


class UserActivationToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expired_at = models.DateTimeField()

    objects = UserActivationTokenManager()
