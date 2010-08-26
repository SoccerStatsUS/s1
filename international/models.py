from django.db import models

from soccer.places.models import Country

class Confederation(models.Model):
    full_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('short_name',)

    def __unicode__(self):
        return self.short_name


# Not using national teamms yet.  Not sure where these should go.

#class Team(models.Model):
#    confederation = models.ForeignKey(Confederation, related_name='teams')
#    country = models.ForeignKey(Country, related_name='teams')
    #ranking = models.IntegerField()

