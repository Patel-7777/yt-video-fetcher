from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_url = models.URLField(unique=True)

    def __str__(self):
        return self.title
