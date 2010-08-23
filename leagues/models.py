from django.db import models

from soccer.international.models import Confederation

class League(models.Model):
    name = models.CharField(max_length=50)
    confederation = models.ForeignKey(Confederation, related_name='leagues')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

