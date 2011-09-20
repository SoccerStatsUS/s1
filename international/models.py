from django.db import models

from soccer.places.models import Country

class Confederation(models.Model):
    """
    A confederation is a confederation.
    """
    full_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('short_name',)

    def __unicode__(self):
        return self.short_name


