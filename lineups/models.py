from django.db import models

from soccer.players.models import Person
from soccer.teams.models import Team


class Game(models.Model):
    date = models.DateField()
    neutral = models.BooleanField()
    
    home_team = models.ForeignKey(Team, related_name="home_games")
    home_score = models.IntegerField()

    away_team = models.ForeignKey(Team, related_name="away_games")
    away_score = models.IntegerField()


    class Meta:
        ordering = ('date',)


    def score(self):
        return "%s - %s" % (self.home_score, self.away_score)

    @property
    def home_players(self):
        return self.gameappearance_set.all()
    

    def __unicode__(self):
        return "%s: %s v %s" % (self.date, self.home_team, self.away_team)



class GameGoal(models.Model):

    game = models.ForeignKey(Game)

    scorer = models.CharField(max_length=255)
    assist_1 = models.CharField(max_length=255)
    assist_2 = models.CharField(max_length=255)
    minute = models.IntegerField()

    def __unicode__(self):
        return "%s: %s" % (self.game, self.minute)

class GamePlayed(models.Model):
    
    game = models.ForeignKey(Game)

    player = models.CharField(max_length=255)
    
    on = models.IntegerField()
    off = models.IntegerField()

    def __unicode__(self):
        return "%s: %s" % (self.game, self.player)


class GoalRecord(models.Model):
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    
    description = models.CharField(max_length=500)
     

class GameAppearance(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Person)

    on = models.IntegerField()
    off = models.IntegerField()
    
    def __unicode__(self):
        return "%s: %s" % (self.game, self.player)
    


    
