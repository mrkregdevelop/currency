from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static

from common.mixins import TestMixin


def avatar_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=TestMixin
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('anonymous-avatar.jpeg')
