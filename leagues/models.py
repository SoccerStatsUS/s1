from django.db import models

from soccer.international.models import Confederation


class Competition(models.Model):
    """
    A competition is something like:
    U.S. Open Cup 1998
    La Liga 2011-2012
    Major League Soccer all-time
    """
    # Or something like that.
    # Not quite sure yet.

    name = models.CharField(max_length=255)

    # types of systems:
    # single-elimination, cup, league, playoffs, etc.
    # Presumably, anything goes.
    system = models.CharField(max_length=255)

    # Do we need a separate season? 2011 or 2010-2011
    # season = models.CharField(max_length=255) 



class League(models.Model):
    """
    A league is a pretty much meaningless construct that we're keeping around
    for now for convenience.
    """
    # I don't really think a team should be listed as belonging to a league;
    # rather, it should participate in a league in a particular year.
    name = models.CharField(max_length=50)
    confederation = models.ForeignKey(Confederation, related_name='leagues')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

