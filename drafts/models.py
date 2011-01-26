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

    def pick_dict(self):
        return dict([(e.player, e.number) for e in self.pick_set.all()])

    def get_missing(self, other_draft):
        missing = {}
        this_picks = self.pick_dict()
        other_picks = other_draft.pick_dict()


        for k, v in this_picks.items():
            if k not in other_picks:
                missing[k] = v

        return sorted(missing.items(), key=lambda e: e[1])
        
    def get_diff(self, other_draft):
        diff = {}
        other_picks = other_draft.pick_dict()

        for k, v in self.pick_dict().items():
            if k in other_picks:
                ov = other_picks[k]
                diff[k] = (v, ov, ov-v)

        return sorted(diff.items(), key=lambda e: e[1][0])


    class Meta:
        ordering = ("name", )
    

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
