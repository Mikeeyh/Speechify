from django.contrib import admin

from Speechify.voices.models import AudioFile


@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    pass

