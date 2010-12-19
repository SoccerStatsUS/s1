from django.db import models

from soccer.teams.models import Team

class Game(models.Model):
    date = models.DateField()
    neutral = models.BooleanField()
    
    home_team = models.ForeignKey(Team, related_name="home_games")
    home_score = models.IntegerField()

    away_team = models.ForeignKey(Team, related_name="away_games")
    away_score = models.IntegerField()


class GameGoal(models.Model):

    game = models.ForeignKey(Game)

    scorer = models.CharField(max_length=255)
    assist_1 = models.CharField(max_length=255)
    assist_2 = models.CharField(max_length=255)
    minute = models.IntegerField()

class GamePlayed(models.Model):
    
    game = models.ForeignKey(Game)

    player = models.CharField(max_length=255)
    
    on = models.IntegerField()
    off = models.IntegerField()


    
