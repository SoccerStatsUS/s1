from django.db import models
from django.forms.models import model_to_dict

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
            

def create_career_stats():
    """Aggregate season stats and save CareerStat instances."""
    # Consider deleting prior stats, transaction management.
    d = career_stats_dict()
    for k, v in d.items():
        # Pass dict as keyword arguments
        cs = CareerStat(**v)
        cs.name = k
        cs.save()


def find_player(model, save=False):
    """Some sort of way to automatically figure out who 
    a given name refers to."""
    from soccer.players.models import Person
    if save:
        p = Person.objects.get_person(model.name)
    else:
        try:
            p = Person.objects.get_person(model.name)
        except:
            print model.name
    # Waiting for errors
    if save:
        model.player = p
        model.save()
    
    

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


    # Season-specific
    team = models.ForeignKey(Team)
    year = models.IntegerField()
    position = models.CharField(max_length=7, default="X")
    number = models.IntegerField(default=-1)
    #base_salary = models.IntegerField(default=0)
    #guaranteed_salary = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s: %s (%s)" % (self.name, self.team, self.year)

    class Meta:
        ordering = ('player', 'year')
            
