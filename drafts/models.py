from django.db import models

from soccer.main.tools import no_player
from soccer.players.models import Person
from soccer.teams.models import Team


class Draft(models.Model):
    """Represents a draft that took place.  
    Consists of a name, a year, and a list of picks
    in sequential order."""
    name = models.CharField(max_length=50, unique=True, null=False)
    year = models.IntegerField()

    def __unicode__(self):
        return self.name
    

class Pick(models.Model):
    """Represents a single pick in a Draft."""
    draft = models.ForeignKey(Draft)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Person, default=no_player)
    name = models.CharField(max_length='250')
    number = models.IntegerField()

    class Meta:
        ordering = ('-draft', 'number')

    def __unicode__(self):
        return "%s:%s (%s)" % (self.number, self.name, self.player)
