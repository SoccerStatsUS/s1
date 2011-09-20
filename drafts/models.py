import datetime

from django.db import models

from soccer.main.tools import no_player
from soccer.players.models import Person
from soccer.teams.models import Team


class Draft(models.Model):
    """
    Represents a draft that took place.  
    Consists of a name, a year, and a list of picks
    in sequential order.
    """

    name = models.CharField(max_length=255, unique=True, null=False)
    draft_type = models.CharField(max_length=255)
    year = models.IntegerField()

    def __unicode__(self):
        return self.name

    def teams(self):
        """
        List all teams from the draft.
        """
        t = [e[0] for e in self.pick_set.all().values_list("team")]
        return Team.objects.filter(id__in=set(t))


    def average_age(self, start=1, end=None):
        """
        Get the average age of something.
        """
        picks = self.pick_set.filter(number__gte=start)
        if end is not None:
            picks = picks.filter(number__lte=end)

        dt = datetime.date(self.year, 1, 1)
        ages = [e.player.age(dt) for e in picks]
        ages = [e for e in ages if e]
        average = sum(ages) / len(ages)
        return average


    @property
    def order_dict(self):
        return dict([(e.player, e.number) for e in self.pick_set.all()])

    @property
    def team_dict(self):
        return dict([(e.player, e.team) for e in self.pick_set.all()])


    def get_missing(self, other_draft):
        """
        Get some sort of missing thing.
        """
        missing = {}
        this_picks = self.order_dict
        other_picks = other_draft.order_dict


        for k, v in this_picks.items():
            if k not in other_picks:
                missing[k] = v

        return sorted(missing.items(), key=lambda e: e[1])
        
    def get_diff(self, other_draft):
        """
        """
        diff = {}
        other_picks = other_draft.order_dict

        team_dict = self.team_dict

        for k, v in self.order_dict.items():
            team = team_dict[k]
            if k in other_picks:
                ov = other_picks[k]
                diff[k] = (v, ov, ov-v, team)
            else:
                diff[k] = (v, '', '', team)

        return sorted(diff.items(), key=lambda e: e[1][0])

    def score_draft(self, other_draft):
        """
        Comparing drafts by score, vaguely.
        For USMNT draft.
        """

        # ?
        next_order = other_draft.order_dict

        order_ids = {}
        for k,v in next_order.items():
            order_ids[k.id] = v
            
            
        max_pick = len(next_order) + 1

        # Sort picks by team.
        d = {}
        for team, picks in self.by_team():
            picks = [order_ids.get(p.player.id, max_pick) for p in picks]
            d[team] = sorted(picks)


        scores = []
        # Presumably because there are 11 drafters?
        for team, picks in d.items():
            p = picks[:11] # ?
            average = sum(p) / 11.0
            median = p[6]
            scores.append((team, average, median))

        scores = sorted(scores, key=lambda e: e[1])

        return scores
            
            

    def by_team(self):
        l = []
        teams = sorted(set([e.team for e in self.pick_set.all()]))
        for team in teams:
            picks = self.pick_set.filter(team=team)
            l.append((team.name, picks))
        return l


    class Meta:
        ordering = ("name", )
    

# A perfect model?
# Other methods useful?
class Pick(models.Model):
    """
    Represents a single pick in a Draft.
    """

    draft = models.ForeignKey(Draft)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Person, default=no_player)
    name = models.CharField(max_length='250')
    number = models.IntegerField()

    class Meta:
        ordering = ('-draft', 'number')

    def __unicode__(self):
        return "%s:%s (%s)" % (self.number, self.name, self.player)
