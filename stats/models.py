from django.db import models
from django.db.models.signals import post_save
from django.db.transaction import commit_on_success
from django.forms.models import model_to_dict

from soccer.leagues.models import League
from soccer.main.tools import no_player
from soccer.players.models import Person
from soccer.teams.models import Team



def find_aliases():
    # Temporary debugging program
    # Find names that don't work.
    m = SeasonStat
    for e in m.objects.all():
        try: find_player(e)
        except: print e


def find_player(model, save=False, attr='name'):
    """
    Some sort of way to automatically figure out who 
    a given name refers to.
    """
    name = getattr(model, attr)
    if save:
        p = Person.objects.get_person(name)
        model.player = p
        model.save()
    else:
        try:
            p = Person.objects.get_person(name)
        except:
            print name
    

@commit_on_success
def create_career_stats():
    """Aggregate season stats and save CareerStat instances."""
    # Consider deleting prior stats, transaction management.
    d = career_stats_dict()
    for k, v in d.items():
        # Pass dict as keyword arguments
        cs = CareerStat(**v)
        cs.name = k
        cs.save()    


def career_stats_dict():
    """Populate an empty CareerStats model with career stats for every
    name in SeasonStats"""
    d = {}
    for season in SeasonStat.objects.all():
        sd = model_to_dict(season)
        nd = {}
        # Remove these items from career stats
        excludes = ("player", "team", "position", "year", "number")
        for key, value in sd.items():
            if key not in excludes:
                nd[key] = sd[key]

        # Insert nd into d, either by adding to current values
        # or creating a new entry
        name = nd.pop("name")
        if name not in d:
            d[name] = nd
        else:
            ssd = d[name]
            for key, value in nd.items():
                ssd[key] += value
    return d


# ......................
# Use an abstract model?
# ......................
        
class CareerStat(models.Model):

    # Identity
    name = models.CharField(max_length=250)
    player = models.ForeignKey(Person, default=no_player)

    # Time
    games_played = models.IntegerField()
    games_started = models.IntegerField()
    minutes = models.IntegerField()

    # Scoring
    goals = models.IntegerField()
    game_winning_goals = models.IntegerField()
    assists = models.IntegerField()
    shots = models.IntegerField()
    shots_on_goal = models.IntegerField()

    # Fouls
    fouls_committed = models.IntegerField()
    fouls_suffered = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    # Miscellaneous
    offsides = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalty_attempts = models.IntegerField()

    # Goalkeeping
    shutouts = models.IntegerField()
    goals_allowed = models.IntegerField()
    shots_faced = models.IntegerField()
    saves = models.IntegerField()
    penalties_allowed = models.IntegerField()
    penalties_faced = models.IntegerField()

    def __unicode__(self):
        return self.name


class SeasonStat(models.Model):

    # Identity
    name = models.CharField(max_length=250)
    player = models.ForeignKey(Person, default=no_player)

    # Time
    games_played = models.IntegerField()
    games_started = models.IntegerField()
    minutes = models.IntegerField()

    # Scoring
    goals = models.IntegerField()
    game_winning_goals = models.IntegerField()
    assists = models.IntegerField()
    shots = models.IntegerField()
    shots_on_goal = models.IntegerField()

    # Fouls
    fouls_committed = models.IntegerField()
    fouls_suffered = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    # Miscellaneous
    offsides = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalty_attempts = models.IntegerField()

    # Goalkeeping
    shutouts = models.IntegerField()
    goals_allowed = models.IntegerField()
    shots_faced = models.IntegerField()
    saves = models.IntegerField()
    penalties_allowed = models.IntegerField()
    penalties_faced = models.IntegerField()


    # Season-specific
    team = models.ForeignKey(Team)
    year = models.IntegerField()
    position = models.CharField(max_length=7, default="X")
    number = models.IntegerField(default=-1)

    def __unicode__(self):
        return "%s: %s (%s)" % (self.name, self.team, self.year)


    class Meta:
        ordering = ('player', 'year')


class SeasonTotalManager(models.Manager):
    pass
    


class SeasonTotal(models.Model):
    year = models.IntegerField()
    league = models.ForeignKey(League)

    # Time
    games_played = models.IntegerField()
    games_started = models.IntegerField()
    minutes = models.IntegerField()

    # Scoring
    goals = models.IntegerField()
    game_winning_goals = models.IntegerField()
    assists = models.IntegerField()
    shots = models.IntegerField()
    shots_on_goal = models.IntegerField()

    # Fouls
    fouls_committed = models.IntegerField()
    fouls_suffered = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    # Miscellaneous
    offsides = models.IntegerField()
    penalty_goals = models.IntegerField()
    penalty_attempts = models.IntegerField()

    # Goalkeeping
    shutouts = models.IntegerField()
    goals_allowed = models.IntegerField()
    shots_faced = models.IntegerField()
    saves = models.IntegerField()
    penalties_allowed = models.IntegerField()
    penalties_faced = models.IntegerField()

    # Misc.
    objects = SeasonTotalManager()






class GameStat(models.Model):
    # Identity
    name = models.CharField(max_length=250)
    player = models.ForeignKey(Person, default=no_player)

    # Scoring
    goals = models.IntegerField()
    assists = models.IntegerField()
    shots = models.IntegerField()
    shots_on_goal = models.IntegerField()
    
    corner_kicks = models.IntegerField(default=0)
    crosses = models.IntegerField(default=0)
    offsides = models.IntegerField(default=0)

    # Fouls
    fouls_committed = models.IntegerField()
    fouls_suffered = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    # Goalkeeping
    saves = models.IntegerField(default=0)
    
