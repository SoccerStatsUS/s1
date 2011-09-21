from django.db import models

class Video(models.Model):
    """
    It's a video.
    """
    
    url = models.CharField(max_length=1023)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
