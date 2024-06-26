import os

from django.contrib.auth import get_user_model
from django.db import models

from Speechify.core.models import IHaveUser
from Speechify.profiles.models import Profile


UserModel = get_user_model()


class AudioFile(models.Model):
    text = models.TextField(
        max_length=255,
    )

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    audio_file = models.FileField(
        upload_to='audio_files/',
        # null=True,
        # blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Done only on `create`
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    # ADDING:
    def filename(self):
        return os.path.basename(self.audio_file.name)

    # def __str__(self):
    #     return self.title
