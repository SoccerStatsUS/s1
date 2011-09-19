from django.db import models

from soccer.teams.models import Team


# Oh no! I've created a second game model here.
# But really, games deserves its own model.
# It shouldn't just be a subset of 
class Game(models.Model):
    """
    A separate game model.
    """
    # Should we have a date and a datetime field?
    date = models.DateField()
    
    #neutral = models.BooleanField(default=False)
    
    home_team = models.ForeignKey(Team, related_name="home_games2")
    home_score = models.IntegerField()

    away_team = models.ForeignKey(Team, related_name="away_games2")
    away_score = models.IntegerField()

    # These should perhaps be foreign keys. Maybe one day.
    location = models.CharField(max_length=255)
    competition = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        ordering = ('date',)
        unique_together = [('home_team', 'date'), ('away_team', 'date')]


    def score(self):
        return "%s - %s" % (self.home_score, self.away_score)

    #@property
    #def home_players(self):
    #    return self.gameappearance_set.all()
    

    def __unicode__(self):
        return u"%s: %s v %s" % (self.date, self.home_team, self.away_team)



