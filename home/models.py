from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class youtube_video(models.Model):
    title = models.CharField(max_length=100)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)